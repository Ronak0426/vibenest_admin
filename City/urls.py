from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/add_city', views.add_city),
    path('adminpanel/view_city', views.view_city),
    path('adminpanel/insert_city', views.insertCity),
    path('adminpanel/update_city/<int:id>', views.update_city),
    path('adminpanel/delete_city/<int:id>', views.deletecity),
    path('adminpanel/save_city/<int:id>', views.save_city),
    path('adminpanel/loadcitybystate', views.loadcitybystate),
]
