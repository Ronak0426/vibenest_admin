from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import States
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/adminpanel")
def add_states(request):
    return render(request,'admin/add_states.html')

@login_required(login_url="/adminpanel")
def insertStates(request):
    state_name = request.POST.get("txtstaname")

    #Duplication
    if States.objects.filter(state_name = state_name).exists():
        messages.error(request,"State already exist!")
    else:
        #Image Upload
        image = request.FILES["txtstaimage"]
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        fileurl = fs.url(file)

        obj = States()
        obj.state_name = state_name
        obj.state_image = fileurl
        obj.save()
        messages.success(request,"State Added Successfully!")
    return redirect("/adminpanel/add_states")

@login_required(login_url="/adminpanel")
def view_states(request):
    data = States.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_states.html',context)

@login_required(login_url="/adminpanel")
def deletestate(request,id):
    obj = States.objects.filter(state_id = id).get()
    imagename = obj.state_image

    file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(str(imagename)))
    if os.path.exists(file_path):
        os.remove(file_path)
    obj.delete()
    messages.success(request,"State Delete Successfully!")
    return redirect("/adminpanel/view_states")

@login_required(login_url="/adminpanel")
def update_state(request,id):
    obj = States.objects.filter(state_id = id).get()
    context = {
        "stateobj" : obj
    }
    return render(request,'admin/update_state.html',context)

@login_required(login_url="/adminpanel")
def save_state(request,id):
    obj = States.objects.filter(state_id = id).get()
    fileurl = ""
    if len(request.FILES) == 0:
        fileurl = obj.state_image
    else:
        #Old Image Delete
        imagename = obj.state_image
        file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(str(imagename)))
        if os.path.exists(file_path):
            os.remove(file_path)
        #New Image Uploaded
        image = request.FILES["txtstaimage"]
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        fileurl = fs.url(file)
        
    state_name = request.POST.get("txtstaname")
    obj = States.objects.filter(state_id = id).get()
    obj.state_name = state_name
    obj.state_image = fileurl
    obj.save()
    messages.success(request,"State Updated Successfully!")
    return redirect("/adminpanel/view_states")