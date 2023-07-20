from django.shortcuts import render
from .messages.publish import publish_message, publish_control_state, publish_confirm_state
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    
    created_engagements = {
        "1":"Achat Vehicule",
        "2":"Renovation Batiment"
    }

    return render(request, 'myapp/index.html',{
        'eng': created_engagements
    })

def create_engagement(request):
    name = request.POST.get('name', '')

    publish_message(name)
    print("Message sent")

    return HttpResponseRedirect(reverse("myapp:index"))

def control_engagement(request, id):
    eng_id = request.POST.get('eng_id', '')

    publish_control_state(eng_id)

    print("Engagement Controlled")

    return HttpResponseRedirect(reverse("myapp:index"))

def confirm_engagement(request, id):
    eng_id = request.POST.get('eng_id', '')

    publish_confirm_state(eng_id)

    print("Engagement Confirm")

    return HttpResponseRedirect(reverse("myapp:index"))

