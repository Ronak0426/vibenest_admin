from django.shortcuts import render

# Create your views here.
def loadhome(request):
    return render(request,'user/home.html')