# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Notification

@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk = notification_id)
        notification.is_read = True
        notification.save()

        if  notification.notification_type == Notification.MESSAGE:
            return redirect('conversation', user_id = notification.created_by.id)
        elif notification.notification_type == Notification.FOLLOWER:
            return redirect('oinkerprofile', username= notification.created_by.username)
        # Note: reason why we have separate methods 'created_by', 'to_user' is because
        # to_user redirects it to your page whereas 'created_by' is to another user    
        elif notification.notification_type == Notification.LIKE:
            return redirect( 'oinkerprofile', username= notification.to_user.username)
        elif notification.notification_type == Notification.MENTION:
            return redirect('oinkerprofile', username= notification.created_by.username)


        
    return render(request, 'notification/notifications.html')