import os

import boto3

from boto3.dynamodb.conditions import Key

from chalice import WebsocketDisconnectedError

class Storage(object):
    def __init__(self, table):

        self._table = table

    @classmethod
    def from_env(cls):
        table_name = os.environ.get('TABLE', '')
        table = boto3.resource('dynamodb').Table(table_name)
        return cls(table)

    def create_connection(self, connection_id):
        self._table.put_item(
            Item={
                'PK': connection_id,
                'SK': 'username_',
            },
        )
    
    def set_username(self, connection_id, old_name, username):
        self._table.delete_item(
            Key={
                'PK': connection_id,
                'SK': 'username_%s' % old_name,
            },
        )
        self._table.put_item(
            Item={
                'PK': connection_id,
                'SK': 'username_%s' % old_name,
            },
        )

    def set_position(self, connection_id, x, y):
        """Set the room a user is currently in.

        The room a user is in is in the form of an SK that starts with
        room_ prefix.

        :param connection_id: The connection id to move to a room.

        :param room: The room name to join.
        """
        try:
            r = self._table.query(
                KeyConditionExpression=(
                    Key('PK').eq(connection_id)
                ),
                Select='ALL_ATTRIBUTES',
            )
            for item in r['Items']:
                if 'position' in item['SK']:
                    self._table.delete_item(
                        Key={
                            'PK': connection_id,
                            'SK': item['SK'],
                        },
                    )
        except Exception as e:
            print(e)

        self._table.put_item(
            Item={
                'PK': connection_id,
                'SK': f'position_{x}_{y}',
            },
        )

    # def list_rooms(self):
    #     """Get a list of all rooms that exist.

    #     Scan through the table looking for SKs that start with room_
    #     which indicates a room that a user is in. Collect a unique set
    #     of those and return them.
    #     """
    #     # r = self._table.scan()
    #     rooms = set([item['SK'].split('_', 1)[1] for item in r['Items']
    #                  if item['SK'].startswith('room_')])
    #     return rooms

    # def set_room(self, connection_id, room):
    #     """Set the room a user is currently in.

    #     The room a user is in is in the form of an SK that starts with
    #     room_ prefix.

    #     :param connection_id: The connection id to move to a room.

    #     :param room: The room name to join.
    #     """
    #     self._table.put_item(
    #         Item={
    #             'PK': connection_id,
    #             'SK': 'room_%s' % room,
    #         },
    #     )

    # def remove_room(self, connection_id, room):
    #     """Remove a user from a room.

    #     The room a user is in is in the form of an SK that starts with
    #     room_ prefix. To leave a room we need to delete this entry.

    #     :param connection_id: The connection id to move to a room.

    #     :param room: The room name to join.
    #     """
    #     self._table.delete_item(
    #         Key={
    #             'PK': connection_id,
    #             'SK': 'room_%s' % room,
    #         },
    #     )

    # def get_connection_ids_by_room(self, room):
    #     """Find all connection ids that go to a room.

    #     This is needed whenever we broadcast to a room. We collect all
    #     their connection ids so we can send messages to them. We use a
    #     ReverseLookup table here which inverts the PK, SK relationship
    #     creating a partition called room_{room}. Everything in that
    #     partition is a connection in the room.

    #     :param room: Room name to get all connection ids from.
    #     """
    #     r = self._table.query(
    #         IndexName='ReverseLookup',
    #         KeyConditionExpression=(
    #             Key('SK').eq('room_%s' % room)
    #         ),
    #         Select='ALL_ATTRIBUTES',
    #     )
    #     return [item['PK'] for item in r['Items']]

    def get_connections(self):
        print('GETTING CONNECTIONS')
        r = self._table.scan()
        print(r)
        connections = set([item['PK'] for item in r['Items']])
        print(connections)
        return connections


    def delete_connection(self, connection_id):
        try:
            r = self._table.query(
                KeyConditionExpression=(
                    Key('PK').eq(connection_id)
                ),
                Select='ALL_ATTRIBUTES',
            )
            for item in r['Items']:
                self._table.delete_item(
                    Key={
                        'PK': connection_id,
                        'SK': item['SK'],
                    },
                )
        except Exception as e:
            print(e)

    def get_record_by_connection(self, connection_id):
        """Get all the properties associated with a connection.

        Each connection_id creates a partition in the table with multiple
        SK entries. Each SK entry is in the format {property}_{value}.
        This method reads all those records from the database and puts them
        all into dictionary and returns it.

        :param connection_id: The connection to get properties for.
        """
        r = self._table.query(
            KeyConditionExpression=(
                Key('PK').eq(connection_id)
            ),
            Select='ALL_ATTRIBUTES',
        )
        r = {
            entry['SK'].split('_', 1)[0]: entry['SK'].split('_', 1)[1]
            for entry in r['Items']
        }
        return r

class Sender(object):
    """Class to send messages over websockets."""
    def __init__(self, app, storage):
        """Initialize a sender object.

        :param app: A Chalice application object.

        :param storage: A Storage object.
        """
        self._app = app
        self._storage = storage

    def send(self, connection_id, message):
        """Send a message over a websocket.

        :param connection_id: API Gateway Connection ID to send a
            message to.

        :param message: The message to send to the connection.
        """
        try:
            # Call the chalice websocket api send method
            self._app.websocket_api.send(connection_id, message)
        except WebsocketDisconnectedError as e:
            # If the websocket has been closed, we delete the connection
            # from our database.
            self._storage.delete_connection(e.connection_id)

    def broadcast(self, connection_ids, message):
        """"Send a message to multiple connections.

        :param connection_id: A list of API Gateway Connection IDs to
            send the message to.

        :param message: The message to send to the connections.
        """
        print('BROADCASTING CONNECTIONS')
        print(connection_ids)
        for cid in connection_ids:
            print(cid)
            self.send(cid, message)

class Handler(object):
    """Handler object that handles messages received from a websocket.

    This class implements the bulk of our app behavior.
    """
    def __init__(self, storage, sender):
        """Initialize a Handler object.

        :param storage: Storage object to interact with database.

        :param sender: Sender object to send messages to websockets.
        """
        self._storage = storage
        self._sender = sender
        # Command table to translate a string command name into a
        # method to call.
        self._command_table = {
            'move': self._move
            # 'help': self._help,
            # 'nick': self._nick,
            # 'join': self._join,
            # 'room': self._room,
            # 'quit': self._quit,
            # 'ls': self._list,
        }
    
    def handle(self, connection_id, message):
        """Entry point for our application.

        :param connection_id: Connection id that the message came from.

        :param message: Message we got from the connection.
        """
        # First look the user up in the database and get a record for it.
        record = self._storage.get_record_by_connection(connection_id)
        # if record['username'] == '':
        #     # If the user does not have a username, we assume that the message
        #     # is the username they want and we call _handle_login_message.
        #     self._handle_login_message(connection_id, message)
        # else:
            # Otherwise we assume the user is logged in. So we call
            # a method to handle the message. We pass along the
            # record we loaded from the database so we don't need to
            # again.
            # self._handle_message(connection_id, message, record)
        self._move(connection_id, message, record)

    def _move(self, connection_id, message, record):
        args = message.split(' ')
        x = args[0]
        y = args[1]

        self._storage.set_position(connection_id, x, y)
        connection_ids = self._storage.get_connections()
        print(connection_ids)
        msg = f'{x} {y}'
        self._sender.broadcast(connection_ids, msg)

    # def _handle_login_message(self, connection_id, message):
    #     """Handle a login message.

    #     The message is the username to give the user. Re-write the
    #     database entry for this user to reset their username from ''
    #     to {message}. Once that is done send a message back to the user
    #     to confirm the name choice. Also send a /help prompt.
    #     """
    #     self._storage.set_username(connection_id, '', message)
    #     self._sender.send(
    #         connection_id,
    #         'Using nickname: %s\nType /help for list of commands.' % message
    #     )

    # def _handle_message(self, connection_id, message, record):
    #     """"Handle a message from a connected and logged in user.

    #     If the message starts with a / it's a command. Otherwise its a
    #     text message to send to all rooms in the room.

    #     :param connection_id: Connection id that the message came from.

    #     :param message: Message we got from the connection.

    #     :param record: A data record about the sender.
    #     """
        # if message.startswith('/'):
        #     self._handle_command(connection_id, message[1:], record)
        # else:
        #     self._handle_text(connection_id, message, record)

    # def _handle_command(self, connection_id, message, record):
    #     """Handle a command message.

    #     Check the command name and look it up in our command table.
    #     If there is an entry, we call that method and pass along
    #     the connection_id, arguments, and the loaded record.

    #     :param connection_id: Connection id that the message came from.

    #     :param message: Message we got from the connection.

    #     :param record: A data record about the sender.
    #     """
    #     args = message.split(' ')
    #     command_name = args.pop(0).lower()
    #     command = self._command_table.get(command_name)
    #     if command:
    #         command(connection_id, args, record)
    #     else:
    #         # If no command method is found, send an error message
    #         # back to the user.
    #         self._sender(
    #             connection_id, 'Unknown command: %s' % command_name)

    # def _handle_text(self, connection_id, message, record):
    #     """Handle a raw text message.

    #     :param connection_id: Connection id that the message came from.

    #     :param message: Message we got from the connection.

    #     :param record: A data record about the sender.
    #     """
    #     if 'room' not in record:
    #         # If the user is not in a room send them an error message
    #         # and return early.
    #         self._sender.send(
    #             connection_id, 'Cannot send message if not in chatroom.')
    #         return
    #     # Collect a list of connection_ids in the same room as the message
    #     # sender.
    #     connection_ids = self._storage.get_connection_ids_by_room(
    #         record['room'])
    #     # Prefix the message with the sender's name.
    #     message = '%s: %s' % (record['username'], message)
    #     # Broadcast the new message to everyone in the room.
    #     self._sender.broadcast(connection_ids, message)

    # def _help(self, connection_id, _message, _record):
    #     """Send the help message.

    #     Build a help message and send back to the same connection.

    #     :param connection_id: Connection id that the message came from.
    #     """
    #     self._sender.send(
    #         connection_id,
    #         '\n'.join([
    #             'Commands available:',
    #             '    /help',
    #             '          Display this message.',
    #             '    /join {chat_room_name}',
    #             '          Join a chatroom named {chat_room_name}.',
    #             '    /nick {nickname}',
    #             '          Change your name to {nickname}. If no {nickname}',
    #             '          is provided then your current name will be printed',
    #             '    /room',
    #             '          Print out the name of the room you are currently ',
    #             '          in.',
    #             '    /ls',
    #             '          If you are in a room, list all users also in the',
    #             '          room. Otherwise, list all rooms.',
    #             '    /quit',
    #             '          Leave current room.',
    #             '',
    #             'If you are in a room, raw text messages that do not start ',
    #             'with a / will be sent to everyone else in the room.',
    #         ]),
    #     )

    # def _nick(self, connection_id, args, record):
    #     """Change or check nickname (username).

    #     :param connection_id: Connection id that the message came from.

    #     :param args: Argument list that came after the command.

    #     :param record: A data record about the sender.
    #     """
    #     if not args:
    #         # If a nickname argument was not provided, we just want to
    #         # report the current nickname to the user.
    #         self._sender.send(
    #             connection_id, 'Current nickname: %s' % record['username'])
    #         return
    #     # The first argument is assumed to be the new desired nickname.
    #     nick = args[0]
    #     # Change the username from record['username'] to nick in the storage
    #     # layer.
    #     self._storage.set_username(connection_id, record['username'], nick)
    #     # Send a message to the requestor to confirm the nickname change.
    #     self._sender.send(connection_id, 'Nickname is: %s' % nick)
    #     # Get the room the user is in.
    #     room = record.get('room')
    #     if room:
    #         # If the user was in a room, announce to the room they have
    #         # changed their name. Don't send this me sage to the user since
    #         # they already got a name change message.
    #         room_connections = self._storage.get_connection_ids_by_room(room)
    #         room_connections.remove(connection_id)
    #         self._sender.broadcast(
    #             room_connections,
    #             '%s is now known as %s.' % (record['username'], nick))

    # def _join(self, connection_id, args, record):
    #     """Join a chat room.

    #     :param connection_id: Connection id that the message came from.

    #     :param args: Argument list. The first argument should be the
    #        name of the room to join.

    #     :param record: A data record about the sender.
    #     """
    #     # Get the room name to join.
    #     room = args[0]
    #     # Call quit to leave the current room we are in if there is any.
    #     self._quit(connection_id, '', record)
    #     # Get a list of connections in the target chat room.
    #     room_connections = self._storage.get_connection_ids_by_room(room)
    #     # Join the target chat room.
    #     self._storage.set_room(connection_id, room)
    #     # Send a message to the requestor that they have joined the room.
    #     # At the same time send an announcement to everyone who was already
    #     # in the room to alert them of the new user.
    #     self._sender.send(
    #         connection_id, 'Joined chat room "%s"' % room)
    #     message = '%s joined room.' % record['username']
    #     self._sender.broadcast(room_connections, message)

    # def _room(self, connection_id, _args, record):
    #     """Report the name of the current room.

    #     :param connection_id: Connection id that the message came from.

    #     :param record: A data record about the sender.
    #     """
    #     if 'room' in record:
    #         # If the user is in a room send them the name back.
    #         self._sender.send(connection_id, record['room'])
    #     else:
    #         # If the user is not in a room. Tell them so, and how to
    #         # join a room.
    #         self._sender.send(
    #             connection_id,
    #             'Not currently in a room. Type /join {room_name} to do so.'
    #         )

    # def _quit(self, connection_id, _args, record):
    #     """Quit from a room.

    #     :param connection_id: Connection id that the message came from.

    #     :param record: A data record about the sender.
    #     """
    #     if 'room' not in record:
    #         # If the user is not in a room there is nothing to do.
    #         return
    #     # Find the current room name, and delete that entry from
    #     # the database.
    #     room_name = record['room']
    #     self._storage.remove_room(connection_id, room_name)
    #     # Send a message to the user to inform them they left the room.
    #     self._sender.send(
    #         connection_id, 'Left chat room "%s"' % room_name)
    #     # Tell everyone in the room that the user has left.
    #     self._sender.broadcast(
    #         self._storage.get_connection_ids_by_room(room_name),
    #         '%s left room.' % record['username'],
    #     )

    # def _list(self, connection_id, _args, record):
    #     """Show a context dependent listing.

    #     :param connection_id: Connection id that the message came from.

    #     :param record: A data record about the sender.
    #     """
    #     room = record.get('room')
    #     if room:
    #         # If the user is in a room, get a listing of everyone
    #         # in the room.
    #         result = [
    #             self._storage.get_record_by_connection(c_id)['username']
    #             for c_id in self._storage.get_connection_ids_by_room(room)
    #         ]
    #     else:
    #         # If they are not in a room. Get a listing of all rooms
    #         # currently open.
    #         result = self._storage.list_rooms()
    #     # Send the result list back to the requestor.
    #     self._sender.send(connection_id, '\n'.join(result))