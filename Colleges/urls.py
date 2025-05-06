from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('adminpanel/add_colleges', views.add_colleges),
    path('adminpanel/view_colleges', views.view_colleges),
    path('adminpanel/insert_colleges', views.insertColleges),
    path('adminpanel/update_colleges/<int:id>', views.update_colleges),
    path('adminpanel/delete_colleges/<int:id>', views.deletecolleges),
    path('adminpanel/save_colleges/<int:id>',views.save_colleges),
]