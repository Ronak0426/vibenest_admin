from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('adminpanel/add_category', views.add_category),
    path('adminpanel/view_category', views.view_category),
    path('adminpanel/insert_category', views.insertCategory), 
    path('adminpanel/update_category/<int:id>', views.update_category),
    path('adminpanel/delete_category/<int:id>', views.deletecategory),   
    path('adminpanel/save_category/<int:id>', views.save_category),
]