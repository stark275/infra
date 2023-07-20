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

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",    
        database="compta",
        port="33077"
    )

def getDb():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",    
        database="compta",
        port="33077"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO engagements (name) VALUES (%s)"
    val = ("achat Vehicule",)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def execute(request):
    # cursor = getDb()
    print(request)

def callback(ch, method, props, body):
    print("[-] Receved: %r" % body)

    mycursor = mydb.cursor()
    clean_query =  str(body)[1:].replace("'","")
    mycursor.execute(clean_query)
    mydb.commit()

    print(mycursor.rowcount, "success!")

    


channel.basic_consume(
    queue='db.execute',
    on_message_callback=callback,
    auto_ack=True)

print('[+] Waiting for messages From DBE')
# getDb()
channel.start_consuming() 