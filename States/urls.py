from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/add_states', views.add_states),
    path('adminpanel/view_states', views.view_states),
    path('adminpanel/insert_state', views.insertStates),
    path('adminpanel/update_state/<int:id>',views.update_state),
    path('adminpanel/delete_state/<int:id>', views.deletestate),
    path('adminpanel/save_state/<int:id>',views.save_state),
]