from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Degrees
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/adminpanel")
def add_degrees(request):
    return render(request,'admin/add_degrees.html')

@login_required(login_url="/adminpanel")
def insertDegree(request):
    degree_name = request.POST.get("txtdegname")
    obj = Degrees()
    obj.degree_name = degree_name
    obj.save()
    messages.success(request, "Degree Added Successfully!")
    return redirect("/adminpanel/add_degrees")
    
@login_required(login_url="/adminpanel")
def view_degrees(request):
    data = Degrees.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_degrees.html',context)

@login_required(login_url="/adminpanel")
def deletedegree(request,id):
    Degrees.objects.filter(degree_id = id).delete()
    messages.success(request,"Degree Delete Successfully!")
    return redirect("/adminpanel/view_degrees")

@login_required(login_url="/adminpanel")
def update_degree(request,id):
    obj = Degrees.objects.filter(degree_id = id).get()
    context = {
        "degreeobj": obj
    }
    return render(request,'admin/update_degree.html',context)

@login_required(login_url="/adminpanel")
def save_degree(request,id):
    degree_name = request.POST.get("txtdegname")
    obj = Degrees.objects.filter(degree_id = id).get()
    obj.degree_name = degree_name
    obj.save()
    messages.success(request, "Degree Updated Successfully!")
    return redirect("/adminpanel/view_degrees")

