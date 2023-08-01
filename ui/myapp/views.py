from django.shortcuts import render
from .messages.publish import publish_message, publish_control_state, publish_confirm_state
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Engagement
import mysql.connector 


# Create your views here.
def index(request):

    mydb = getDb()
    
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM engagements WHERE created='v' AND controlled='f' AND confirmed='f'")

    created_engs = mycursor.fetchall()
    print(created_engs)

    mycursor.execute("SELECT * FROM engagements WHERE created='v' AND controlled='v' AND confirmed='f'")

    controlled_engs = mycursor.fetchall()

   
    return render(request, 'myapp/index.html',{
        'engs': created_engs,
        'controlled' : controlled_engs
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

    publish_confirm_state(eng_id)

    print("Engagement Confirmed")

    return HttpResponseRedirect(reverse("myapp:index"))

def getDb():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",    
        database="compta",
        port="3306"
    )
    

