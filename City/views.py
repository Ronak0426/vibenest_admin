from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import City
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from States.models import States
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required(login_url="/adminpanel")
def add_city(request):
    statedata = States.objects.all()
    context = {
        "statedata":statedata
    }
    return render(request,'admin/add_city.html',context)

@login_required(login_url="/adminpanel")
def insertCity(request):
    city_name = request.POST.get("txtcityname")
    sid = request.POST.get("txtstateid")

    #duplication
    if City.objects.filter(city_name = city_name).exists():
        messages.error(request,"City already exist!")
    else:
        obj = City()
        obj.city_name = city_name
        obj.state_id = States.objects.filter(state_id = sid).get()
        obj.save()
        messages.success(request,"City Added Successfully!")
    return redirect("/adminpanel/add_city")

@login_required(login_url="/adminpanel")
def view_city(request):
    data = City.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_city.html',context)

@login_required(login_url="/adminpanel")
def deletecity(request,id):
    City.objects.filter(city_id = id).delete()
    messages.success(request,"City Delete Successfully!")
    return redirect("/adminpanel/view_city")

@login_required(login_url="/adminpanel")
def update_city(request,id):
    obj = City.objects.filter(city_id = id).get()
    statedata = States.objects.all()
    context = {
        "cityobj": obj,
        "statedata":statedata
    }
    return render(request,'admin/update_city.html',context)

@login_required(login_url="/adminpanel")
def save_city(request,id):
    obj = City.objects.filter(city_id = id).get()
    city_name = request.POST.get("txtcityname")
    sid = request.POST.get("txtstateid")
    obj.city_name = city_name
    obj.state_id = States.objects.filter(state_id = sid).get()
    obj.save()
    messages.success(request,"City Updated Successfully!")
    return redirect("/adminpanel/view_city")

@csrf_exempt
def loadcitybystate(request):
    stateid = request.POST.get("stateid")
    cid = request.POST.get("cid")
    citydata = City.objects.filter(state_id = stateid)
    output = "<option value=''>Please Select City</option>"
    for row in citydata:
        if str(cid) == str(row.city_id):
            output = output + "<option selected value='"+str(row.city_id)+"'>"+row.city_name+"</option>"
        else:
            output = output + "<option value='"+str(row.city_id)+"'>"+row.city_name+"</option>"
    return HttpResponse(output)