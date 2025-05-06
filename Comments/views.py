from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Comments
from Posts.models import Posts
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required(login_url="/adminpanel")
def view_comments(request):
    data = Comments.objects.all()
    context = {
        "data":data
    }
    return render(request,'admin/view_comment.html',context)

@login_required(login_url="/adminpanel")
def delete_comments(request,id):
    Comments.objects.filter(comment_id = id).delete()
    messages.success(request,"Comments Delete Successfully!")
    return redirect("/adminpanel/view_comments")