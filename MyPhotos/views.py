from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from.models import MyPhotos
import os
from django.conf import settings
from django.contrib import messages


# Create your views here.
def myphotos(request):
    photo = MyPhotos.objects.filter(user_id = request.user.id)
    context = {
        "photo":photo
    }
    return render(request,'mainuser/myphotos.html',context)

def insert_photos(request):

        #Image Upload
        image = request.FILES["img"]
        fs = FileSystemStorage()
        file = fs.save(image.name,image)
        fileurl = fs.url(file)

        obj = MyPhotos()
        obj.photo_url = fileurl
        obj.user_id = User.objects.get(id = request.user.id)
        obj.save()
        return redirect("/myphotos")

def delete_photo(request,id):
    obj = MyPhotos.objects.filter(photo_id = id).get()
    imagename = obj.photo_url

    file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(str(imagename)))
    if os.path.exists(file_path):
        os.remove(file_path)
    obj.delete()
    return redirect("/myphotos")