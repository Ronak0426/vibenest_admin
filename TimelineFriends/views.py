from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from ExtraInfo.models import ExtraInfo


# Create your views here.
def timelinefriends(request,id):
    userdata = User.objects.get(id=id)
    data = User.objects.all()
    extrainfo = ExtraInfo.objects.all()
    userextrainfo = ExtraInfo.objects.get(user_id=id)
    context = {
        "data":data,
        "extrainfo":extrainfo,
        "userdata":userdata, 
        "userextrainfo":userextrainfo,   
        "id":id
    }
    return render(request,'user/timelinefriends.html',context)