from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url="/adminpanel")

def view_alluser(request):
    data = User.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_alluser.html',context)

def deletealluser(request,id):
    User.objects.filter(id = id).delete()
    messages.success(request,"User Delete Successfully!")
    return redirect("/adminpanel/view_alluser")