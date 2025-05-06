from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/view_postusercat', views.view_postusercat),
    path('adminpanel/delete_postusercat/<int:id>', views.delete_postusercat),


     path('insert_postusercat', views.insert_postusercat),
     path('postusercat', views.postusercat),
]