from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel', views.myprofile),
    path('adminpanel/checkadminlogin', views.checkadminlogin),
    path('adminpanel/checklogout', views.checklogout),
]