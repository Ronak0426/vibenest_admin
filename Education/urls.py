from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_education', views.view_education),
    path('adminpanel/delete_education/<int:id>', views.delete_education),
]