from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.loginpage),
    path('register', views.register),
    path('signup', views.signup),
    path('checklogin', views.checklogin),
    path('logoutuser', views.logoutuser),
    path('lockpage', views.lockpage),
    path('forgotpassword',views.forgotpassword),
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='mainuser/password_reset_form.html'), 
         name='password_reset'),

    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='mainuser/password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='mainuser/password_reset_confirm.html'), 
         name='password_reset_confirm'),

    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='mainuser/password_reset_complete.html'), 
         name='password_reset_complete'),
]