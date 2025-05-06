from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Career
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/adminpanel")

def view_career(request):
    data = Career.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_career.html',context)

@login_required(login_url="/adminpanel")

def delete_career(request,id):
    Career.objects.filter(career_id = id).delete()
    messages.success(request,"Career Delete Successfully!")
    return redirect("/adminpanel/view_career")
