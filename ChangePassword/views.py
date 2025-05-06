from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
@login_required(login_url="/adminpanel")
def changepassword(request):
    return render(request,'admin/changepassword.html')

def updatepassword(request):
    oldpwd = request.POST.get("oldpwd")
    newpwd = request.POST.get("newpwd")
    user = authenticate(username=request.user.username, password=oldpwd)
    if user is not None:
        user.set_password(newpwd)
        user.save()
        messages.success(request,"Password updated")  
    else:
        messages.error(request,"Old password not match")
    return redirect("/adminpanel/changepassword")
        




    