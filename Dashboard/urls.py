from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('adminpanel/dashboard', views.loadDashboard),
    path('adminpanel/reports', views.loadReport)
]
