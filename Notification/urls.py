from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('adminpanel/add_notification', views.add_notification),
    path('adminpanel/view_notification', views.view_notification),
    path('adminpanel/insert_notification', views.insert_notification),
    path('adminpanel/update_notification/<int:id>', views.update_notification),
    path('adminpanel/delete_notification/<int:id>', views.delete_notification),
    path('adminpanel/save_notification/<int:id>', views.save_notification),
    
]