from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_groups', views.view_groups),
    path('adminpanel/delete_groups/<int:id>', views.delete_groups),
]