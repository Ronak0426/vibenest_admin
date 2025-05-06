from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_socialtime', views.view_socialtime),
    path('adminpanel/delete_socialtime/<int:id>', views.delete_socialtime),
]