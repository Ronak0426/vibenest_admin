from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_likes', views.view_likes),
    path('adminpanel/delete_likes/<int:id>', views.delete_likes),
]