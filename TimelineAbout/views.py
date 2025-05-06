from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from ExtraInfo.models import ExtraInfo
from Education.models import Education
from Career.models import Career
from Friends.models import Friends
from Notification.models import Notification
import datetime

# Create your views here.
def timelineabout(request,id):    
    data = User.objects.get(id=id)
    extrainfo = ExtraInfo.objects.get(user_id=id)
    education = Education.objects.filter(user_id=id)
    career = Career.objects.filter(user_id=id)
    context = {
        "data":data,
        "extrainfo":extrainfo,
        "education":education,
        "id":id,
        "career":career
    }    
    return render(request,'user/timelineabout.html',context)

def addafriend(request):
    fid = request.POST.get("fid")
    obj = Friends()
    obj.status = "pending"
    obj.f_datetime = datetime.datetime.now()
    obj.friend_id = User.objects.get(id = fid)
    obj.user_id = User.objects.get(id=request.user.id)
    obj.save()


    obj = Friends()
    obj.status = "accept"
    obj.f_datetime = datetime.datetime.now()
    obj.friend_id = User.objects.get(id=request.user.id)
    obj.user_id = User.objects.get(id = fid)
    obj.save()

    obj = Notification()
    obj.title = "New Friend request!"
    udata = User.objects.get(id = fid)
    obj.description = "New friend request from " + udata.first_name
    obj.category = "Friend Request"
    obj.noti_datetime = datetime.datetime.now()
    obj.user_id = User.objects.get(id=fid)
    obj.save()

    return redirect("/newsfeed")




