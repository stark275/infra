import pika
import mysql.connector

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





def getDb():
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="compta"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO engagements (name) VALUES (%s)"
    val = ("achat mobilier",)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def execute(request):
    # cursor = getDb()
    print(request)

def callback(ch, method, props, body):
    print("[-] Receved: %r" % body)
    execute("Ce personnage est important")


channel.basic_consume(
    queue='db.execute',
    on_message_callback=callback,
    auto_ack=True)

print('[+] Waiting for messages')
getDb()
channel.start_consuming() 