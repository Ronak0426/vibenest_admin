from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/adminpanel")
def add_category(request):
    return render(request,'admin/add_category.html')

@login_required(login_url="/adminpanel")
def insertCategory(request):
    category_name = request.POST.get("txtcatname")

    #Image Upload
    image = request.FILES["txtcatimage"]
    fs = FileSystemStorage()
    file = fs.save(image.name,image)
    fileurl = fs.url(file)

    obj = Category()
    obj.category_name = category_name
    obj.category_image = fileurl
    obj.save()
    messages.success(request,"Category Added Successfully!")
    return redirect("/adminpanel/add_category") 

@login_required(login_url="/adminpanel")
def view_category(request):
    data = Category.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_category.html',context)

@login_required(login_url="/adminpanel")
def deletecategory(request,id):
    obj = Category.objects.filter(category_id = id).get()
    imagename = obj.category_image

    file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(str(imagename)))
    if os.path.exists(file_path):
        os.remove(file_path)
    obj.delete()
    messages.success(request,"Category Delete Successfully!")
    return redirect("/adminpanel/view_category")

@login_required(login_url="/adminpanel")
def update_category(request,id):
    obj = Category.objects.filter(category_id = id).get()
    context = {
        "categoryobj": obj
    }
    return render(request,'admin/update_category.html',context)

@login_required(login_url="/adminpanel")
def save_category(request,id):
    obj = Category.objects.filter(category_id = id).get()
    fileurl = ""
    if len(request.FILES) == 0:
        fileurl = obj.category_image
    else:
        #Old Image Delete
        imagename = obj.category_image
        file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(str(imagename)))
        if os.path.exists(file_path):
            os.remove(file_path)
        #New Image Uploaded
        image = request.FILES["txtcatimage"]
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        fileurl = fs.url(file)

    category_name = request.POST.get("txtcatname")
    obj = Category.objects.filter(category_id = id).get()
    obj.category_name = category_name
    obj.category_image = fileurl
    obj.save()
    messages.success(request,"Category Updated Successfully!")
    return redirect("/adminpanel/view_category")
