from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Conversation, ConversationMessage

from django.contrib.auth.models import User


# Create your views here.
@login_required
def conversations(request):
    # Note .conversations method here is taken from the 'related name' parameter in models.py - 'conversations
    # is an index in our database
    conversations = request.user.conversations.all()

    return render(request, 'conversation/conversations.html', {'conversations': conversations})



@login_required
def conversation(request, user_id):
    # define these two methods to check if convo already exists
    conversations = Conversation.objects.filter(users__in = [request.user.id])
    conversations = conversations.filter(users__in = [user_id])
    
    if conversations.count() == 1:
        conversation = conversations[0]
    else:
        recipient = User.objects.get(pk = user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(recipient)
        conversation.save() 
    
    return render(request, 'conversation/conversation.html', {'conversation': conversation})


