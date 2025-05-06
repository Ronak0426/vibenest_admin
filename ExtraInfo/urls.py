from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('adminpanel/view_extrainfo', views.view_extrainfo),
    path('adminpanel/delete_extrainfo/<int:id>', views.delete_extrainfo),
]