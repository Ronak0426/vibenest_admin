from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_career', views.view_career),
    path('adminpanel/delete_career/<int:id>', views.delete_career),
]