from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('timelineabout/<int:id>', views.timelineabout),
    path('addafriend', views.addafriend),
]

    