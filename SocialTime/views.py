from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SocialTime
from django.contrib import messages

# Create your views here.
@login_required(login_url="/adminpanel")
def view_socialtime(request):
    data = SocialTime.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_socialtime.html',context)

@login_required(login_url="/adminpanel")
def delete_socialtime(request,id):
    SocialTime.objects.filter(truck_id = id).delete()
    messages.success(request,"Social Time Details Delete Successfully!")
    return redirect("/adminpanel/view_socialtime")