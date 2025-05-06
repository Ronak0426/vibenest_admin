from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ExtraInfo
from City.models import City

# Create your views here.
@login_required(login_url="/adminpanel")
def view_extrainfo(request):
    data = ExtraInfo.objects.all()
    city = City.objects.all()
    context = {
        "data": data,
        "city":city
    }
    return render(request,'admin/view_extrainfo.html',context)

@login_required(login_url="/adminpanel")
def delete_extrainfo(request,id):
    ExtraInfo.objects.filter(extra_id = id).delete()
    messages.success(request,"Extra Info Delete Successfully!")
    return redirect("/adminpanel/view_extrainfo")



