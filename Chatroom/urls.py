from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('chatroom', views.chatroom),
    path('sendmessage', views.sendmessage),
    path('loadmessages', views.loadmessages),
]