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

exchange_name = 'erp'
created_queue = 'eng.confirmed'
created_route_key = 'confirmed'

dbe_queue= 'db.execute'
dbe_route_key = 'dbe'

channel.exchange_declare(exchange_name, durable=True, exchange_type='topic')

channel.queue_declare(queue=dbe_queue)
channel.queue_bind(exchange=exchange_name, queue=dbe_queue, routing_key=dbe_route_key)

def callback(ch, method, props, body):
    print("[-] Receved: %r" % body)
    ch.basic_publish(
            exchange=exchange_name,
            routing_key=dbe_route_key,
            body= body)
    print("[+] Published on DBE:" )

channel.basic_consume(
    queue=created_queue,
    on_message_callback=callback,
    auto_ack=True)
    
print('[+] Waiting for messages from ConformedDeamon')
channel.start_consuming() 