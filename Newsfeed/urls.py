from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('newsfeed', views.newsfeed),
    path('insert_newsfeed', views.insert_newsfeed),

    path('insert_comment', views.insert_comment),
    path('insert_like/<int:postid>/<str:status>', views.insert_like),
    
    path('insert_likeprofile/<int:postid>/<str:status>/<int:uid>', views.insert_likeprofile)
]

    