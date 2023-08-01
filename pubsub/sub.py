import pika

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

def callback(ch, method, props, body):
    print("[-] Receved: %r" % body)

    # ch.basic_publish(
    #         exchange='archives',
    #         routing_key='dbe',
    #         body= body)

channel.basic_consume(
    queue='auth.service',
    on_message_callback=callback,
    auto_ack=True)

print('[+] Waiting for messages')
channel.start_consuming() 