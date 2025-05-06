from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('myphotos', views.myphotos),
    path('insert_photos', views.insert_photos),
     path('delete_photo/<int:id>', views.delete_photo),
]