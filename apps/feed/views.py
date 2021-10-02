from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

from .models import Oink
# Create your views here

@login_required
def feed(request):
    userids = [request.user.id]
    # for everyone I follow, add their user ids to this list:
    for oinker in request.user.oinkerprofile.follows.all():
        userids.append(oinker.user.id)
    oinks = Oink.objects.filter(created_by_id__in = userids )

    for oink in oinks:
        likes = oink.likes.filter(created_by_id = request.user.id)

        if likes.count() > 0:
            oink.liked = True
        else: 
            oink.liked = False

    return render(request, 'feed/feed.html', {'oinks': oinks})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0: 
        oinkers = User.objects.filter(username__icontains = query)
        oinks = Oink.objects.filter(body__icontains = query)
    else: 
        oinkers = []
        oinks = []
    context = {
        'query': query,
        'oinkers': oinkers,
        'oinks': oinks
    }
    return render(request, 'feed/search.html', context)