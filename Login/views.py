from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from SocialTime.models import SocialTime
import datetime
from django.contrib.auth import authenticate,login,logout
from django.db.models import F, ExpressionWrapper, fields
from django.utils.timezone import now
from ExtraInfo.models import ExtraInfo


# Create your views here.
def loginpage(request):
    return render(request,'mainuser/login.html')
def signup(request):
    return render(request,'mainuser/signup.html')
def register(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("email")
    password = request.POST.get("password")

    if User.objects.filter(email=email).exists():
        messages.error(request,"Email ID already Registered")
    else:
        user = User.objects.create_user(first_name = fname,last_name=lname,username = email,email=email,password=password)
        messages.error(request,"Registration successfully!")
    return redirect("/") 

def checklogin(request):
    username = request.POST.get("loginemail")
    password = request.POST.get("loginpassword")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
       
        obj = SocialTime()
        obj.user_id = request.user
        obj.start_datetime = datetime.datetime.now()
        obj.social_date = datetime.datetime.now()
        obj.type='login'
        obj.save()
        request.session['socialid'] = obj.truck_id

        if ExtraInfo.objects.filter(user_id = request.user.id).exists():
            extraobj = ExtraInfo.objects.get(user_id = request.user.id)
            request.session['profileimage'] = extraobj.profile
            extraobj.is_online = "Yes"
            extraobj.save()
            current_date = now().date()
            socialtime_records = SocialTime.objects.filter(
                social_date=current_date,
                user_id = request.user.id,
                start_datetime__isnull=False,
                end_datetime__isnull=False
            )
            annotated_records = socialtime_records.annotate(
                duration_seconds=ExpressionWrapper(
                    F('end_datetime') - F('start_datetime'),
                    output_field=fields.DurationField()
                )
            )
            totalsec = 0.0
            for record in annotated_records:
                duration_in_seconds = record.duration_seconds.total_seconds()
                totalsec = totalsec + duration_in_seconds


            userobj = ExtraInfo.objects.get(user_id = request.user.id)
            timing = int(userobj.timing) * 60
            totalmin = totalsec/60
            print("Total min : " + str(totalmin))
            print("Total Timing : " + str(timing))
            if(totalmin<=timing):
                return redirect("/newsfeed")
            else:
                return redirect("/lockpage")
        request.session['profileimage'] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmRLRMXynnc7D6-xfdpeaoEUeon2FaU0XtPg&s"

        
        return redirect("/newsfeed")

        
    else:
        messages.error(request,"Email or password not found!!")
        return redirect("/") 

def logoutuser(request):
        if ExtraInfo.objects.filter(user_id = request.user.id).exists():
            extraobj = ExtraInfo.objects.get(user_id = request.user.id)
            obj = SocialTime.objects.get(truck_id =  request.session.get('socialid', ''))
            obj.end_datetime = datetime.datetime.now()
            obj.type='logout'
            extraobj.is_online = "No"
            extraobj.save()
            obj.save()
            logout(request)
        return redirect("/") 
    
def lockpage(request):
     return render(request,'mainuser/lockpage.html')

def forgotpassword(request):
    return render(request,'mainuser/forgotpassword.html')
