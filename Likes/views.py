from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Likes

# Create your views here.
@login_required(login_url="/adminpanel")
def view_likes(request):
    data = Likes.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_likes.html',context)

@login_required(login_url="/adminpanel")
def delete_likes(request,id):
    Likes.objects.filter(lid = id).delete()
    messages.success(request,"Like Delete Successfully!")
    return redirect("/adminpanel/view_likes")