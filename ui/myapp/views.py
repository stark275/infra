from django.shortcuts import render
from .messages.publish import publish_message, publish_control_state, publish_confirm_state
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Engagement
import mysql.connector 


# Create your views here.
def index(request):

    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",    
        database="compta",
        port="3306"
    )
    
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM engagements WHERE created='v' AND controlled='f' AND confirmed='f'")

    created_engs = mycursor.fetchall()
    print(created_engs)

    

    created_engagements = {
        "1":"Achat Vehicule",
        "6":"Renovation Batiment"
    }

    return render(request, 'myapp/index.html',{
        'eng': created_engagements,
        'engs': created_engs,
    })

def create_engagement(request):
    name = request.POST.get('name', '')

    publish_message(name)
    print("Message sent")

    return HttpResponseRedirect(reverse("myapp:index"))

def control_engagement(request, id):
    eng_id = request.POST.get('eng_id', '')

    # print(eng_id)
    publish_control_state(eng_id)

    print("Engagement Controlled")

    return HttpResponseRedirect(reverse("myapp:index"))

def confirm_engagement(request, id):
    eng_id = request.POST.get('eng_id', '')

    # publish_confirm_state(eng_id)

    print("Engagement Confirmed")

    return HttpResponseRedirect(reverse("myapp:index"))

def getDb():
    
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO engagements (name) VALUES (%s)"
    val = ("achat Vehicule",)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

