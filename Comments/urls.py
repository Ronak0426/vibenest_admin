from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_comments', views.view_comments),
    path('adminpanel/delete_comments/<int:id>', views.delete_comments),
    
]