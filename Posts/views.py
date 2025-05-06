from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Posts
from django.contrib import messages
from Category.models import Category
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/adminpanel")
def view_posts(request):
    data = Posts.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_post.html',context)

@login_required(login_url="/adminpanel")
def delete_posts(request,id):
    Posts.objects.filter(post_id = id).delete()
    messages.success(request,"Post Delete Successfully!")
    return redirect("/adminpanel/view_posts")