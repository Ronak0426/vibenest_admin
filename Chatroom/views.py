from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from ExtraInfo.models import ExtraInfo
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from Friends.models import Friends
# Create your views here.
def chatroom(request):
    data = Friends.objects.filter(user_id = request.user.id,status='accept')
    #data = User.objects.exclude(id = request.user.id)
    extrainfo = ExtraInfo.objects.all()
    context = {
        "data":data,
        "extrainfo":extrainfo,
        "totalfriends":len(data)
    }
    return render(request,'mainuser/chatroom.html',context)

@csrf_exempt
def sendmessage(request):
    current_user = request.POST.get("current_user")
    message = request.POST.get("message")
    other_user = request.POST.get("other_user")

    obj = Message()
    obj.message = message
    obj.receiver = User.objects.get(id = other_user)
    obj.sender = User.objects.get(id = current_user)
    obj.save()

    return JsonResponse({"message": message, "sender_id": current_user})

@csrf_exempt    
def loadmessages(request):
    current_user = request.POST.get("current_user")
    other_user = request.POST.get("other_user")

    other = User.objects.get(id = other_user)
    current = User.objects.get(id = current_user)

    messages = (
    Message.objects.filter(sender=request.user, receiver=other_user).values() |
    Message.objects.filter(sender=other_user, receiver=request.user).values()
    ).order_by("timestamp")
    return JsonResponse(list(messages),safe=False)

    


