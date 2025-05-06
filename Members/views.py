from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Members
from django.contrib import messages

# Create your views here.
@login_required(login_url="/adminpanel")
def view_members(request):
    data = Members.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_members.html',context)

@login_required(login_url="/adminpanel")
def delete_members(request,id):
    Members.objects.filter(member_id = id).delete()
    messages.success(request,"Member Delete Successfully!")
    return redirect("/adminpanel/view_members")