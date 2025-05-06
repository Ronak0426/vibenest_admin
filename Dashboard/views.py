from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from Groups.models import UserGroups
from Colleges.models import Colleges
from Category.models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/adminpanel")
def loadDashboard(request):
    userdata = User.objects.all()
    group = UserGroups.objects.all()
    college = Colleges.objects.all()
    category = Category.objects.all()
    context={
        "totaluser":len(userdata),
        "group":len(group),
        "userdata":userdata,
        "college":len(college),
        "category":len(category)
    }
    return render(request,'admin/dashboard.html',context)

@login_required(login_url="/adminpanel")

def loadReport(request):
    return render(request,'admin/reports.html')