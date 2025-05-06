from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_posts', views.view_posts),
    path('adminpanel/delete_posts/<int:id>', views.delete_posts),
]