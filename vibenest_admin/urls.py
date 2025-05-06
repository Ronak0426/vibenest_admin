"""
URL configuration for vibenest_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Dashboard.urls')),
    path('',include('City.urls')),
    path('',include('States.urls')),
    path('',include('Category.urls')),
    path('',include('Colleges.urls')),
    path('',include('Degrees.urls')),
    path('',include('Posts.urls')),
    path('',include('Comments.urls')),
    path('',include('Likes.urls')),
    path('',include('Groups.urls')),
    path('',include('Members.urls')),
    path('',include('Notification.urls')),
    path('',include('AllUser.urls')),
    path('',include('Career.urls')),
    path('',include('Education.urls')),
    path('',include('Friends.urls')),
    path('',include('SocialTime.urls')),
    path('',include('ExtraInfo.urls')),
    path('',include('PostUserCat.urls')),
    path('',include('Home.urls')),
    path('',include('Login.urls')),
    path('',include('ChangePassword.urls')),
    path('',include('MyProfile.urls')),
    path('',include('Newsfeed.urls')),
    path('',include('FriendSuggestion.urls')),
    path('',include('MyFriend.urls')),
    path('',include('Chatroom.urls')),
    path('',include('FAQPage.urls')),
    path('',include('EditProfile.urls')),  
    path('',include('Timeline.urls')),
    path('',include('TimelineAbout.urls')),
    path('',include('TimelineFriends.urls')),   
    path('',include('Contact.urls')),
    path('',include('MyPhotos.urls')),
    path('',include('GroupChat.urls')),
]



# only in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)