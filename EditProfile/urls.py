from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('basicinfo', views.basicinfo),
    path('education', views.education),
    path('career', views.career),
    path('groups', views.groups),
    path('myinterests', views.myinterests),
    path('accountsetting', views.accountsetting),
    path('changepassword', views.changepassword),

    path('insert_basicinfo', views.insert_basicinfo),
    path('insert_education', views.insert_education),
    path('insert_career', views.insert_career), 
    path('insert_groups', views.insert_groups),

    path('update_password', views.update_password),

    path('userpost', views.userpost),
    path('userabout', views.userabout),
    path('userfriendfollowing', views.userfriendfollowing),
    path('myfriendlist', views.myfriendlist),
    path('myfriendprofile/<int:id>', views.myfriendprofile),
    path('myfriendrequest', views.myfriendrequest),
    path('myfriendrequestprofile/<int:id>', views.myfriendrequestprofile),
    path('myfriendsuggestion', views.myfriendsuggestion),
    path('searchfriendsuggestion', views.searchfriendsuggestion),
    path('group', views.group),
    path('groupdetails/<int:id>', views.groupdetails),
    path('grouprequest', views.grouprequest),
    path('notification', views.notification),
    path('delete_notification/<int:id>', views.delete_notification),
    path('editprofile', views.editprofile),
    path('userfriendrequest', views.userfriendrequest),
    path('changefriendstatus', views.changefriendstatus),
    path('changegroupstatus', views.changegroupstatus),
    path('leavegroup', views.leavegroup),
    path('getnotification', views.getnotification),


    path('add_member/<int:id>', views.add_member),
    path('delete_education/<int:id>', views.delete_education)
]
