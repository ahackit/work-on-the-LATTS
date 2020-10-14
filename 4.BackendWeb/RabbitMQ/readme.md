# RabbitMQ

- RabbitMQ is a message broker, it accepts and forwards messages.
- Producing means a program that produces a message.
- Queue is the name of where all the messages are stored.
- Consumer is a program that waits for a message.
- Can use many different languages to interact with Rabbit, Pike is the recommended.

## Basic Connection/Sending/Receiving
### Connection
- Connection code looks the same for producers/consumers
```
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
```
### Sending
- Messages can never be sent to the queue directly, have to go through exchanges.
```
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
```
### Consuming
- When consuming, yo should redeclare queues to make sure it exists
```
channel.queue_declare(queue='hello')
``
- When consuming, you must provide callbacks.
```
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
```
- Start consumer, and don't stop it.
```
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
```

## Work Queues
- This is about declaring tasks to be ran later.
- Example below is delaying task by seconds using ...
```
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)
```
```
import time

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
```

### Message (Ack)knowledgement
- If a worker dies with a message, you want to make sure your Message queue knows bout it.
```
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep( body.count('.') )
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='hello', on_message_callback=callback)
```
### Message Durability
- Makes messages non-ephemeral
```
channel.queue_declare(queue='task_queue', durable=True)
```
```
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
```

### Fair Dispatch
- This makes workers only get one job and not have many piling up.
```
channel.basic_qos(prefetch_count=1)
```
## Publish/Subscribe
- This model is about publishing messages to many queues/consumers
- Exchanges control how messages are published to queue(s)

### Exchange
- direct, topic, headers and fanout are types of exchanges
- Fanout sends to all queues.
```
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
```

- Create temporary Queue

```
result = channel.queue_declare(queue='')
```

- Set exclusive flag to delete the temporary queue

```
result = channel.queue_declare(queue='', exclusive=True)
```

- Create binding

```
channel.queue_bind(exchange='logs',
                   queue=result.method.queue)
```

## Routing
- Routing is the ability to filter the type of messages we consume using Routes
```
channel.queue_bind(exchange=exchange_name,
                   queue=queue_name,
                   routing_key='black')
```
```
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
```