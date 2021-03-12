# from boto3.session import Session
# from chalice import WebsocketDisconnectedError
# from chalice import Chalice



# app = Chalice(app_name='sockettest')
# app.websocket_api.session = Session()
# app.experimental_feature_flags.update([
#     'WEBSOCKETS'
# ])


# @app.on_ws_message()
# def message(event):
#     try:
#         app.websocket_api.send(
#             connection_id=event.connection_id,
#             message=event.body,
#         )
#     except WebsocketDisconnectedError as e:
#         pass


from boto3.session import Session
from chalice import Chalice
from chalicelib import Storage
from chalicelib import Sender
from chalicelib import Handler

app = Chalice(app_name="sockettest")
app.debug = True
app.websocket_api.session = Session()
app.experimental_feature_flags.update([
    'WEBSOCKETS'
])

STORAGE = Storage.from_env()
SENDER = Sender(app, STORAGE)
HANDLER = Handler(STORAGE, SENDER)

@app.on_ws_connect()
def connect(event):
    STORAGE.create_connection(event.connection_id)

@app.on_ws_disconnect()
def disconnect(event):
    STORAGE.delete_connection(event.connection_id)

@app.on_ws_message()
def message(event):
    HANDLER.handle(event.connection_id, event.body)
