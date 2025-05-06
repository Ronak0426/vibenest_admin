from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Colleges
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/adminpanel")
def add_colleges(request):
    return render(request,'admin/add_colleges.html')

@login_required(login_url="/adminpanel")
def insertColleges(request):
    colleges_name = request.POST.get("txtclgname")

    #Image Upload
    image = request.FILES["txtclgimage"]
    fs = FileSystemStorage()
    file = fs.save(image.name,image)
    fileurl = fs.url(file)

    obj = Colleges()
    obj.colleges_name = colleges_name
    obj.colleges_logo = fileurl
    obj.save()
    messages.success(request,"College Added Successfully!")
    return redirect("/adminpanel/add_colleges")

@login_required(login_url="/adminpanel")
def view_colleges(request):
    data = Colleges.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_colleges.html',context)

@login_required(login_url="/adminpanel")
def deletecolleges(request,id):
    obj = Colleges.objects.filter(colleges_id = id).get()
    imagename = obj.colleges_logo

    file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(str(imagename)))
    if os.path.exists(file_path):
        os.remove(file_path)
    obj.delete()
    messages.success(request,"College  Delete Successfully!")
    return redirect("/adminpanel/view_colleges")

@login_required(login_url="/adminpanel")
def update_colleges(request,id):
    obj = Colleges.objects.filter(colleges_id = id).get()
    context = {
        "collegesobj": obj
    }
    return render(request,'admin/update_colleges.html',context)

@login_required(login_url="/adminpanel")
def save_colleges(request,id):
    obj = Colleges.objects.filter(colleges_id = id).get()
    fileurl = ""
    if len(request.FILES) == 0:
        fileurl = obj.colleges_logo
    else:
        #Old Image Delete
        imagename = obj.colleges_logo
        file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(str(imagename)))
        if os.path.exists(file_path):
            os.remove(file_path)
        #New Image Uploaded
        image = request.FILES["txtclgimage"]
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        fileurl = fs.url(file)
        
    colleges_name = request.POST.get("txtclgname")
    obj = Colleges.objects.filter(colleges_id = id).get()
    obj.colleges_name = colleges_name
    obj.colleges_logo = fileurl
    obj.save()
    messages.success(request,"College Updated Successfully!")
    return redirect("/adminpanel/view_colleges")