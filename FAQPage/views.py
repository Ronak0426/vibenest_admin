from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def FAQpage(request):
    return render(request,'mainuser/FAQpage.html')

def termsandconditions(request):
    return render(request,'mainuser/termsandconditions.html')

def aboutus(request):
    return render(request,'mainuser/about.html')
