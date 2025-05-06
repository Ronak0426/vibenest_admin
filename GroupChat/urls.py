from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('groupchat', views.groupchat),
    path('sendgroupmessage', views.sendgroupmessage),
    path('loadgroupmessages', views.loadgroupmessages),
    
]