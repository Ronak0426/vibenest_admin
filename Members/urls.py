from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_members', views.view_members),
    path('adminpanel/delete_members/<int:id>', views.delete_members),
]