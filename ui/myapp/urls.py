from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    # ex: /dashboard/
    path("", views.index, name="index"),
    path("create-engagement/", views.create_engagement, name="create_engagement"),
    path("control-engagement/<int:id>", views.control_engagement, name="control_engagement"),
    path("confirm-engagement/<int:id>", views.confirm_engagement, name="confirm_engagement"),
]