from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserGroups

# Create your views here.
@login_required(login_url="/adminpanel")
def view_groups(request):
    data = UserGroups.objects.all()
    context = {
        "data": data
    }
    return render(request,'admin/view_groups.html',context)

@login_required(login_url="/adminpanel")
def delete_groups(request,id):
    UserGroups.objects.filter(groups_id = id).delete()
    messages.success(request,"Groups Delete Successfully!")
    return redirect("/adminpanel/view_groups")