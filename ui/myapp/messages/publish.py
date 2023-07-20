import pika

credentials = pika.PlainCredentials('guest', 'guest')
connexion = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='194.163.143.59',
        port=5672,
        virtual_host='/',
        credentials=credentials
    )
)

channel = connexion.channel()

exchange = 'erp'


# Connection a l'exchange appelé message, qui est durable et qui a le type topic
channel.exchange_declare(exchange, durable=True, exchange_type='topic')

################################################################################
queue_name = 'eng.created'
route_key = 'created'

channel.queue_declare(queue= queue_name)
channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=route_key)

#################################################################################
controlled_queue = 'eng.controlled'
controlled_route_key = 'controlled'

channel.queue_declare(queue=controlled_queue)
channel.queue_bind(exchange=exchange, queue=controlled_queue, routing_key=controlled_route_key)

#################################################################################

confirmed_queue = 'eng.confirmed'
confirmed_route_key = 'confirmed'

channel.queue_declare(queue=confirmed_queue )
channel.queue_bind(exchange=exchange, queue=confirmed_queue , routing_key=confirmed_route_key)



def publish_message(message):

    query = 'INSERT INTO engagements(name,created) VALUES("'+str(message)+'","v")'
    channel.basic_publish(
        exchange=exchange,
        routing_key=route_key,
        body=query 
    )
    
    print(message)

def publish_control_state(message):

    

    channel.basic_publish(
        exchange=exchange,
        routing_key=controlled_route_key,
        body=message 
    )

def publish_confirm_state(message):
    channel.basic_publish(
        exchange=exchange,
        routing_key=confirmed_route_key,
        body=message 
    )