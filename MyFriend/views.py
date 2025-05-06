from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from ExtraInfo.models import ExtraInfo
from Education.models import Education

# Create your views here.
def myfriend(request):
    data = User.objects.all()
    extrainfo = ExtraInfo.objects.all()
    education = Education.objects.all()
    context = {
        "data":data,
        "extrainfo":extrainfo,
        "education":education
    }
    return render(request,'user/myfriend.html',context)

