from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('FAQpage', views.FAQpage),
    path('termsandconditions', views.termsandconditions),
    path('aboutus', views.aboutus),

]

    