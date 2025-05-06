from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_friends', views.view_friends),
    path('adminpanel/delete_friends/<int:id>', views.delete_friends),
]