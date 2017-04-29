from django.shortcuts import render, redirect
from Profile.models import Profile

def profile_page(request, user_name):
    try:
        profile = Profile.objects.get(user__username=user_name)
        context = {'profile': profile.user}
    except Profile.DoesNotExist:
        context = {'profile': None}
    return render(request, 'profile.html', context)