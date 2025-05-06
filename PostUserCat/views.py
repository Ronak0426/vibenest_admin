from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import PostUserCat
from Category.models import Category
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required(login_url="/adminpanel")
def view_postusercat(request):
    data = PostUserCat.objects.all()
    context = {
        "data": data
    }
    return render(request,'admin/view_postusercat.html',context)

@login_required(login_url="/adminpanel")
def delete_postusercat(request,id):
    PostUserCat.objects.filter(userpostcat_id = id).delete()
    messages.success(request,"Post User Category Delete Successfully!")
    return redirect("/adminpanel/view_postusercat")


def postusercat(request):
    category = Category.objects.all()
    context = {
        "category":category

    }
    return render(request,'mainuser/newsfeed.html',context)

def insert_postusercat(request):
    if request.method == "POST":
        category_id = request.POST.get("category")
        if not category_id:
            return HttpResponse("Category ID is required.", status=400)

        category = get_object_or_404(Category, pk=category_id)

        # Create the PostUserCat instance
        post_user_cat = PostUserCat.objects.create(
            user_id=request.user,
            category_id=category
        )

        return redirect("/newsfeed", status=201)
    else:
        return HttpResponse("Invalid request method.", status=405)


# def insert_postusercat(request):
#     category_id = request.POST.get("category")

#     obj = PostUserCat()
#     obj.category_id = Category.objects.filter(category_id = category_id).get()
#     obj.user_id = User.objects.get(request.user_id=id)
#     obj.save()
