from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Notification

# Create your views here.
@login_required(login_url="/adminpanel")
def add_notification(request):
    userdata = User.objects.all()
    context = {
        "userdata":userdata
    }
    return render(request,'admin/add_notification.html',context)

@login_required(login_url="/adminpanel")
def insert_notification(request):
    title = request.POST.get("txtnotitle")
    description = request.POST.get("txtnotides")
    category = request.POST.get("txtcategory")
    userid = request.POST.get("userid")

    #duplication
    if Notification.objects.filter(title = title).exists():
        messages.error(request,"Notification already exist!")
    else:
        obj = Notification()
        obj.title = title
        obj.description = description
        obj.category = category
        obj.user_id = User.objects.get(id=userid)
        obj.save()
        messages.success(request,"Notification Added Successfully!")
        return redirect("/adminpanel/add_notification")

@login_required(login_url="/adminpanel")
def view_notification(request):
    data = Notification.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_notification.html',context)

@login_required(login_url="/adminpanel")
def delete_notification(request,id):
    Notification.objects.filter(notification_id = id).delete()
    messages.success(request,"Notification Delete Successfully!")
    return redirect("/adminpanel/view_notification")

@login_required(login_url="/adminpanel")
def save_notification(request,id):
    obj = Notification.objects.get(notification_id = id)
    title = request.POST.get("txtnotitle")
    description = request.POST.get("txtnotides")
    category = request.POST.get("txtcategory")
    userid = request.POST.get("userid")
    obj.title = title
    obj.description = description
    obj.category = category
    obj.user_id = User.objects.get(id=userid)
    obj.save()
    messages.success(request,"Notification Updated Successfully!")
    return redirect("/adminpanel/view_notification")

@login_required(login_url="/adminpanel")
def update_notification(request,id):
    obj = Notification.objects.filter(notification_id = id).get()
    userdata = User.objects.all()
    context = {
        "notificationobj": obj,
        "userdata":userdata
    }
    return render(request,'admin/update_notification.html',context)