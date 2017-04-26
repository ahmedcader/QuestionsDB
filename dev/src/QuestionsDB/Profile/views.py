from django.shortcuts import render, redirect
from Profile.models import Profile

def profile_page(request, id):
    try:
        profile = Profile.objects.get(id=id)
        context = {'profile': profile.user}
    except Profile.DoesNotExist:
        context = {'profile': None}
    return render(request, 'profile.html', context)