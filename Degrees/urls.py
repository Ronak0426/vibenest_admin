from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/add_degrees', views.add_degrees),
    path('adminpanel/view_degrees', views.view_degrees),
    path('adminpanel/insert_degree', views.insertDegree),
    path('adminpanel/update_degree/<int:id>', views.update_degree),
    path('adminpanel/delete_degree/<int:id>', views.deletedegree),
    path('adminpanel/save_degree/<int:id>',views.save_degree),
]