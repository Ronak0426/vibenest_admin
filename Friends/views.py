from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from.models import Friends
from django.contrib import messages

# Create your views here.
@login_required(login_url="/adminpanel")
def view_friends(request):
    data = Friends.objects.all()
    context = {
        "data": data
    }
    return render(request,'admin/view_friends.html',context)

@login_required(login_url="/adminpanel")
def delete_friends(request,id):
    Friends.objects.filter(friends_id = id).delete()
    messages.success(request,"Friends Delete Successfully!")
    return redirect("/adminpanel/view_friends")
