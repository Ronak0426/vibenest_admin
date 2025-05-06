from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    #path('adminpanel/add_city', views.add_city),
    path('adminpanel/changepassword', views.changepassword),
    path('adminpanel/updatepassword', views.updatepassword),
    #path('adminpanel/insert_city', views.insertCity),
    # path('adminpanel/delete_alluser/<int:id>', views.deletealluser),
]