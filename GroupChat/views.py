from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import GroupChat
from django.contrib.auth.models import User
from Groups.models import UserGroups
# Create your views here.
def groupchat(request):
    return render(request,'groupchat.html')

@csrf_exempt
def sendgroupmessage(request):
    current_user = request.POST.get("current_user")
    message = request.POST.get("message")
    groupsid = request.POST.get("groupsid")

    obj = GroupChat()
    obj.groups_id = UserGroups.objects.get(groups_id = groupsid)
    obj.groups_message = message
    obj.sender_id = User.objects.get(id = current_user)
    obj.save()

    return JsonResponse({"message": message, "sender_id": current_user})

@csrf_exempt    
def loadgroupmessages(request):
    groupid = request.POST.get("groupid")
    current_user = request.POST.get("current_user")

    messages = (GroupChat.objects.filter(groups_id = groupid)).order_by("timestamp")
    data = []
    for row in messages:
        obj = {
            "sender_id":row.sender_id.id,
            "groups_message":row.groups_message,
            "sender_id_id":row.sender_id.first_name
        }
        data.append(obj)
    return JsonResponse(data,safe=False)