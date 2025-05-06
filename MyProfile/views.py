from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def myprofile(request):
    return render(request,'admin/myprofile.html')


def checkadminlogin(request):
    uname = request.POST.get("login-username")
    pwd = request.POST.get("login-password")
    user = authenticate(username=uname, password=pwd)
    if user is not None:
        if user.is_superuser == 1:
            login(request, user)
            return redirect("/adminpanel/dashboard")
        else:
            messages.error(request,"Username and password not found")  
    else:
        messages.error(request,"Username and password not found")
    return redirect("/adminpanel")

def checklogout(request):
    logout(request)
    return redirect("/adminpanel")