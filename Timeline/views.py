from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from ExtraInfo.models import ExtraInfo
from Posts.models import Posts
import datetime

# Create your views here.
def timeline(request,id):
    data = User.objects.get(id=id)
    extrainfo = ExtraInfo.objects.get(user_id=id)
    posts = Posts.objects.filter(user_id = id)
    #obj.datetime = datetime.datetime.now()
    context = {
        "data":data,
        "extrainfo":extrainfo,
        "posts":posts,
        "id":id
    }
    return render(request,'user/timeline.html',context)