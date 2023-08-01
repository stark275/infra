import pika
import time

i = 0

credentials = pika.PlainCredentials('guest', 'guest')
connexion = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='91.134.181.60',
        port=5672,
        virtual_host='/',
        credentials=credentials
    )
)

channel = connexion.channel()

# Connection a l'exchange appelé message, qui est durable et qui a le type topic
exchange_name = 'erp'
creates_queue = 'eng.created'
create_route_key = 'created'

channel.exchange_declare(exchange_name, durable=True, exchange_type='topic')

channel.queue_declare(queue=creates_queue)
channel.queue_bind(exchange=exchange_name, queue=creates_queue, routing_key=create_route_key)

while(True):
    message = 'SELECT * FROM engagements WHERE name="'+str(i)+'"' 
    time.sleep(2)
    channel.basic_publish(
            exchange=exchange_name,
            routing_key=create_route_key,
            body= message  )
  
    i += 1

    print(message)
    
    # connexion.close()