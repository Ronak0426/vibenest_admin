from django.shortcuts import render,redirect
from django.http import HttpResponse
from Posts.models import Posts
from Category.models import Category
from ExtraInfo.models import ExtraInfo
from Notification.models import Notification
from django.contrib import messages
from django.contrib.auth.models import User
from Comments.models import Comments
from Friends.models import Friends
from Likes.models import Likes
from Groups.models import UserGroups
from django.core.files.storage import FileSystemStorage
import datetime
from Members.models import Members
from PostUserCat.models import PostUserCat
from django.db.models import Subquery
from django.db.models import Q
# Create your views here.

def newsfeed(request):
    fdata = Friends.objects.filter(friend_id = request.user.id,status='Accept')
    category = Category.objects.all()
    friends = Friends.objects.filter(user_id=request.user.id).values_list('friend_id', flat=True)
    data = User.objects.exclude(id = request.user.id).exclude(id__in=friends)
    myfrienddata = Friends.objects.filter(user_id = request.user.id,status='accept').values("friend_id")
    mycategory = PostUserCat.objects.filter(user_id = request.user.id).values("category_id")
    posts = Posts.objects.filter(
        Q(user_id = request.user.id) |
        Q(user_id__in=Subquery(myfrienddata), type="Private") |
        (Q(type="Public") & Q(category_id__in=Subquery(mycategory)))
    ).order_by('-post_id')
    extrainfo = ExtraInfo.objects.all()
    comment = Comments.objects.all()
    likes = Likes.objects.all()


    memgrup = Members.objects.filter(user_id=request.user.id).values('groups_id')
    otherdata = UserGroups.objects.filter(groups_id__in=Subquery(memgrup))
    context = {
        "category":category,
        "data":data,
        "posts":posts,
        "extrainfo":extrainfo,
        "totalcomment":len(comment),
        "comment":comment,
        "likes":likes,
        "otherdata":otherdata,
        "fdata":len(fdata)

    }
    return render(request,'mainuser/newsfeed.html',context)

def insert_newsfeed(request):
    title = request.POST.get("title")
    posttype = request.POST.get("posttype")
    video_url = request.POST.get("vurl")
    text = request.POST.get("text")
    category_id = request.POST.get("category")
    post_date_time = datetime.datetime.now()
    isdisabled = request.POST.get("disable")
    isprivate = request.POST.get("private")
    type = request.POST.get("type")


    #Image Upload'
    fileurl1=fileurl2=fileurl3="dummy.jpg"
    if 'img1' in request.FILES:
        image = request.FILES["img1"]
        fs = FileSystemStorage()
        file1 = fs.save(image.name,image)
        fileurl1 = fs.url(file1)
    if 'img2' in request.FILES:
        image2 = request.FILES["img2"]
        fs = FileSystemStorage()
        file2 = fs.save(image2.name,image2)
        fileurl2 = fs.url(file2)
    if 'img3' in request.FILES:
        image3 = request.FILES["img3"]
        fs = FileSystemStorage()
        file3 = fs.save(image3.name,image3)
        fileurl3 = fs.url(file3)

    

    obj = Posts()
    obj.title = title
    obj.posttype = posttype
    obj.video_url = video_url
    obj.img1 = fileurl1
    obj.img2 = fileurl2
    obj.img3 = fileurl3
    obj.text = "Abc"
    obj.user_id = request.user
    obj.category_id = Category.objects.filter(category_id = category_id).get()
    obj.post_date_time = post_date_time
    obj.isdisabled = isdisabled
    obj.isprivate = isprivate
    obj.type = type
    obj.save()


    data = Friends.objects.filter(user_id = request.user.id,status='accept')
    for row in data:
        obj = Notification()
        obj.title = "New Post Alert!"
        obj.description = "New post added by " + str(request.user.first_name)
        obj.category = "Post"
        obj.noti_datetime = datetime.datetime.now()
        obj.user_id = User.objects.get(id=row.friend_id.id)
        obj.save()

    messages.success(request,"Newsfeed Inserted!")
    return redirect("/newsfeed")

def insert_comment(request):
    comments = request.POST.get("comment")
    post_id = request.POST.get("postid")

    obj=Comments()
    obj.comments = comments
    obj.post_id = Posts.objects.filter(post_id = post_id).get()
    obj.datetime = datetime.datetime.now()
    obj.user_id = request.user
    obj.save()

    postobj = Posts.objects.get(post_id = post_id)
    uid = postobj.user_id.id

    obj = Notification()
    obj.title = "Comment!"
    obj.description = "New comment " + comments
    obj.category = "Comment"
    obj.noti_datetime = datetime.datetime.now()
    obj.user_id = User.objects.get(id=uid)
    obj.save()

    messages.success(request,"Newsfeed Inserted!")
    return redirect("/newsfeed")

def insert_like(request,postid,status):
    obj = Likes()
    obj.post_id = Posts.objects.get(post_id = postid)
    obj.user_id = User.objects.get(id = request.user.id)
    obj.status = status
    obj.save()
    return redirect("/newsfeed")

def insert_likeprofile(request,postid,status,uid):
    obj = Likes()
    obj.post_id = Posts.objects.get(post_id = postid)
    obj.user_id = User.objects.get(id = request.user.id)
    obj.status = status
    obj.save()
    return redirect("/myfriendrequestprofile/"+str(uid))