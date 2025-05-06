from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('friendsuggestion', views.friendsuggestion),
    path('insert_friend/<int:id>', views.insert_friend)

]

    