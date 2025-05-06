from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from Colleges.models import Colleges
from Degrees.models import Degrees
from .models import Education


# Create your views here.
@login_required(login_url="/adminpanel")
def view_education(request):
    data = Education.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_education.html',context)

@login_required(login_url="/adminpanel")
def delete_education(request,id):
    Education.objects.filter(education_id = id).delete()
    messages.success(request,"Education Delete Successfully!")
    return redirect("/adminpanel/view_education")
