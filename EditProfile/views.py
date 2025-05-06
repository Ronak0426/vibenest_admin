from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from City.models import City
from Comments.models import Comments
from Likes.models import Likes
from Friends.models import Friends
from States.models import States
from ExtraInfo.models import ExtraInfo 
from Education.models import Education
from Colleges.models import Colleges
from Degrees.models import Degrees
from Career.models import Career
from django.db.models import Count, Q
from Posts.models import Posts
from MyPhotos.models import MyPhotos
from Groups.models import UserGroups
from Members.models import Members
from Notification.models import Notification
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import datetime
from django.db.models import Subquery
from django.views.decorators.csrf import csrf_exempt
from Category.models import Category

# Create your views here.
def basicinfo(request):
    city = City.objects.all()
    states = States.objects.all()
    if ExtraInfo.objects.filter(user_id = request.user.id).exists():
        data = ExtraInfo.objects.get(user_id = request.user.id)
    else:
        data=None
    context = {
        "city":city,
        "data":data,
        "states":states
    }
    return render(request,'user/basicinfo.html',context)

def insert_basicinfo(request):
    birthdate = request.POST.get("date")
    gender = request.POST.get("optgender")
    cid = request.POST.get("city")
    aboutme = request.POST.get("aboutme")
    timing = request.POST.get("time")

    if ExtraInfo.objects.filter(user_id = request.user.id).exists():
        obj = ExtraInfo.objects.get(user_id = request.user.id)
    else:
        obj = ExtraInfo()

    if 'userphoto' in request.FILES:
        image = request.FILES["userphoto"]
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        fileurl = fs.url(file)
        obj.profile = fileurl

    if 'coverphoto' in request.FILES:
        image = request.FILES["coverphoto"]
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        fileurl = fs.url(file)
        obj.coverphoto = fileurl


    
    obj.birthdate = birthdate
    obj.gender =  gender
    obj.user_id = request.user
    obj.city_id = City.objects.filter(city_id = cid).get()
    obj.aboutme = aboutme
    obj.timing = timing
    obj.save()
    request.session['profileimage'] = obj.profile
    
    messages.success(request,"Basic Information Inserted!")
    return redirect("/editprofile")

def education(request):
    college = Colleges.objects.all()
    degree = Degrees.objects.all()
    data = Education.objects.filter(user_id = request.user.id)
    context = {
        "college":college,
        "degree":degree,
        "data":data
    }
    return render(request,'user/education.html',context)

def insert_education(request):
    colleges_id = request.POST.get("college")
    degree_id = request.POST.get("degree")
    start_year = request.POST.get("start-year")
    end_year = request.POST.get("end-year")
    description = request.POST.get("description")

    obj = Education()
    obj.colleges_id = Colleges.objects.filter(colleges_id = colleges_id).get()
    obj.degree_id = Degrees.objects.filter(degree_id = degree_id).get()
    obj.start_year = start_year 
    obj.end_year = end_year
    obj.description = description
    obj.user_id = request.user
    obj.save()

    messages.success(request,"Education Inserted!")
    return redirect("/editprofile")

def groups(request):
    data = UserGroups.objects.all()
    context = {
        "data":data
    }
    return render(request,'user/groups.html',context)

def career(request):
    return render(request,'user/career.html')

def insert_career(request):
    company_name = request.POST.get("company")
    position = request.POST.get("position")
    start_year = request.POST.get("start-year")
    end_year = request.POST.get("end-year")

    obj = Career()
    obj.company_name = company_name
    obj.position = position
    obj.start_year = start_year
    obj.end_year = end_year
    obj.user_id = request.user
    obj.save()

    messages.success(request,"Career Inserted!")
    return redirect("/editprofile")

def insert_groups(request):
    group_name = request.POST.get("name")
    description = request.POST.get("description")

    #Image Upload
    image = request.FILES["img"]
    fs = FileSystemStorage()
    file = fs.save(image.name,image)
    fileurl = fs.url(file)

    obj = UserGroups()
    obj.group_name = group_name
    obj.description = description
    obj.group_logo = fileurl
    obj.user_id = request.user
    obj.save()

    gid = obj.groups_id
    member = request.user.id
    obj = Members()
    obj.user_id = User.objects.get(id = member)
    obj.groups_id  = UserGroups.objects.get(groups_id=gid)
    obj.status = 'accept'
    obj.f_datetime = datetime.datetime.now()
    obj.save()
    
    return redirect("/group")

def myinterests(request):
    return render(request,'user/myinterests.html')

def accountsetting(request):
    return render(request,'user/accountsetting.html')

def changepassword(request):
    return render(request,'user/changepassword.html')

def update_password(request):
    oldpwd = request.POST.get("oldpwd")
    newpwd = request.POST.get("newpwd")
    user = authenticate(username=request.user.username, password=oldpwd)
    if user is not None:
        user.set_password(newpwd)
        user.save()
        messages.success(request,"Password Updated")  
    else:
        messages.error(request,"Old Password not Match")
    return redirect("/")

def userpost(request):
    return render(request,'user/userpost.html')

def userabout(request):
    data = Friends.objects.filter(user_id = request.user.id)
    if ExtraInfo.objects.filter(user_id = request.user.id).exists():
        pdata = ExtraInfo.objects.get(user_id = request.user.id)
    else:
        pdata=None
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "profiledata":pdata,
        "extrainfo":extrainfo
    }
    return render(request,'user/userabout.html',context)

def userfriendfollowing(request):
    data = Friends.objects.filter(friend_id = request.user.id,status='Accept')
    if ExtraInfo.objects.filter(user_id = request.user.id).exists():
        pdata = ExtraInfo.objects.get(user_id = request.user.id)
    else:
        pdata=None
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "profiledata":pdata,
        "extrainfo":extrainfo
    }
    return render(request,'user/userfriendfollowing.html',context)

def userfriendrequest(request):
    data = Friends.objects.filter(friend_id = request.user.id,status='pending')
    if ExtraInfo.objects.filter(user_id = request.user.id).exists():
        pdata = ExtraInfo.objects.get(user_id = request.user.id)
    else:
        pdata=None
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "profiledata":pdata,
        "extrainfo":extrainfo
    }
    return render(request,'user/userfriendrequest.html',context)

def changefriendstatus(request):
    fid = request.POST.get("fid")
    myid = request.POST.get("myid")
    status = request.POST.get("status")

    obj = Friends.objects.get(friend_id = myid, user_id = fid)
    obj.status = status
    obj.save()
    return redirect("/myfriendlist")

def myfriendlist(request):
    data = Friends.objects.filter(user_id = request.user.id,status='accept')
    extrainfo = ExtraInfo.objects.all()
    education = Education.objects.all()
    context = {
        "data":data,
        "extrainfo":extrainfo,
        "education":education
    }
    return render(request,'mainuser/myfriendlist.html',context)

def myfriendprofile(request,id):
    userdata = User.objects.get(id=id)
    data = User.objects.all()
    extrainfo = ExtraInfo.objects.all()
    userextrainfo = ExtraInfo.objects.get(user_id=id)
    
    context = {
        "data":data,
        "extrainfo":extrainfo,
        "userdata":userdata, 
        "userextrainfo":userextrainfo,   
        "id":id
    }
    return render(request,'mainuser/myfriendprofile.html',context)

def myfriendrequest(request):
    data = Friends.objects.filter(friend_id = request.user.id,status='pending')
    if ExtraInfo.objects.filter(user_id = request.user.id).exists():
        pdata = ExtraInfo.objects.get(user_id = request.user.id)
    else:
        pdata=None
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "profiledata":pdata,
        "extrainfo":extrainfo
    }
    return render(request,'mainuser/myfriendrequest.html',context)

def group(request):
    members_groups_ids = Members.objects.filter(user_id = request.user.id).values('groups_id')
    data = UserGroups.objects.filter(user_id = request.user.id)
    otherdata = UserGroups.objects.filter(groups_id__in=Subquery(members_groups_ids))
    context = {
        "data":data,
        "otherdata":otherdata
    }
    return render(request,'mainuser/group.html',context)

def groupdetails(request,id):
    groupdata = UserGroups.objects.get(groups_id=id)
    members_user_ids = Members.objects.filter(groups_id = id).values('user_id')
    data = Friends.objects.filter(user_id = request.user.id,status='accept').values('friend_id')
    user = User.objects.filter(id__in=Subquery(data)).exclude(id__in=Subquery(members_user_ids))
    extrainfo = ExtraInfo.objects.all()
    userdata = Members.objects.filter(groups_id = id,status='accept')
    context = {
        "groupdata":groupdata,
        "user":user,
        "extrainfo":extrainfo,
        "userdata":userdata
    }
    return render(request,'mainuser/groupdetails.html',context)

def grouprequest(request):
    grpdata = Members.objects.filter(user_id = request.user.id,status='pending')
    context ={
        "grpdata":grpdata
    }
    return render(request,'mainuser/grouprequest.html',context)

def add_member(request,id):
    member = request.POST.get("member")
    obj = Members()
    obj.user_id = User.objects.get(id = member)
    obj.groups_id  = UserGroups.objects.get(groups_id=id)
    obj.status = 'pending'
    obj.f_datetime = datetime.datetime.now()
    obj.save()
    return redirect('/groupdetails/'+str(id))

def changegroupstatus(request):
    gid = request.POST.get("gid")
    uid = request.POST.get("uid")
    status = request.POST.get("status")

    obj = Members.objects.get(groups_id = gid, user_id = uid)
    obj.status = status
    obj.save()
    return redirect("/grouprequest")

def leavegroup(request):
    gid = request.POST.get("gid")
    uid = request.POST.get("uid")

    obj = Members.objects.get(groups_id = gid, user_id = uid)
    obj.delete()
    return redirect("/group")

def notification(request):
    data = Notification.objects.filter(user_id = request.user.id)
    context = {
        "data":data
    }
    return render(request,'mainuser/notification.html',context)
@csrf_exempt
def getnotification(request):
    data = Notification.objects.filter(user_id = request.user.id).values()
    data = list(data)
    return JsonResponse(data,safe=False)


def delete_notification(request,id):
    Notification.objects.filter(notification_id = id).delete()
    return redirect("/notification")

def editprofile(request):
    edudata = Education.objects.filter(user_id = request.user.id)
    cardata = Career.objects.filter(user_id = request.user.id)
    city = City.objects.all()
    states = States.objects.all()
    college = Colleges.objects.all()
    degree = Degrees.objects.all()
    data = Education.objects.filter(user_id = request.user.id)
    if ExtraInfo.objects.filter(user_id = request.user.id).exists():
        data = ExtraInfo.objects.get(user_id = request.user.id)
    else:
        data=None
    context = {
        "city":city,
        "data":data,
        "states":states,
        "college":college,
        "degree":degree,
        "edudata":edudata,
        "cardata":cardata,
        "catdata": Category.objects.all()
    }
    return render(request,'mainuser/editprofile.html',context)

def delete_education(request,id):
    Education.objects.filter(education_id = id).delete()
    messages.success(request,"Education Delete Successfully!")
    return render(request,'mainuser/editprofile.html')

def myfriendrequestprofile(request,id):
    userdata = User.objects.get(id=id)
    #data = User.objects.all()
    #extrainfo = ExtraInfo.objects.all()
    userextrainfo = ExtraInfo.objects.get(user_id=id)

    data = User.objects.get(id=id)
    extrainfo = ExtraInfo.objects.get(user_id=id)
    education = Education.objects.filter(user_id=id)
    career = Career.objects.filter(user_id=id)
    posts = Posts.objects.filter(user_id = id).order_by('-post_id')
    comments = Comments.objects.filter(user_id = id)
    friend = Friends.objects.filter(user_id = id,status='accept')
    friends = ExtraInfo.objects.all()
    photo = MyPhotos.objects.filter(user_id = id)
    allextrainfo = ExtraInfo.objects.all()
    grpdata = UserGroups.objects.filter(user_id = id)
    comment = Comments.objects.all()
    likes = Likes.objects.all()

    context = {
        "data":data,
        "extrainfo":extrainfo,
        "userdata":userdata, 
        "userextrainfo":userextrainfo,   
        "id":id,
        "education":education,
        "career":career,
        "posts":posts,
        "postcount":len(posts),
        "commentcount":len(comments),
        "friendcount":len(friend),
        "friend":friend,
        "friends":friends,
        "photo":photo,
        "allextrainfo":allextrainfo,
        "grpdata":grpdata,
        "comment":comment,
        "likes":likes
    }
    return render(request,'mainuser/myfriendrequestprofile.html',context)


def myfriendsuggestion(request):
    friends = Friends.objects.filter(user_id=request.user.id).values_list('friend_id', flat=True)
    data = User.objects.exclude(id = request.user.id).exclude(id__in=friends).annotate(
        friend_count=Count('user_id', filter=Q(user_id__status='accept'))
    )
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "extrainfo":extrainfo
    }
    return render(request,'mainuser/myfriendsuggestion.html',context)

def searchfriendsuggestion(request):
    q = request.GET.get("q")
    friends = Friends.objects.filter(user_id=request.user.id).values_list('friend_id', flat=True)
    data = User.objects.exclude(id = request.user.id).exclude(id__in=friends)
    if q:
        data = data.filter(first_name__icontains=q)
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "extrainfo":extrainfo
    }
    return render(request,'mainuser/searchfriendsuggestion.html',context)