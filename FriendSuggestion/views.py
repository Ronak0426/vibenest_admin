from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from Friends.models import Friends
from ExtraInfo.models import ExtraInfo
import datetime

# Create your views here.
def friendsuggestion(request):
    data = User.objects.all()
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "extrainfo":extrainfo
    }
    return render(request,'user/friendsuggestion.html',context)

def insert_friend(request,id):
    obj = Friends()
    obj.user_id = request.user
    obj.friend_id = User.objects.get(id = id)
    obj.status = 'pending'
    obj.f_datetime = datetime.datetime.now()
    obj.save()
    return redirect("/friendsuggestion")

