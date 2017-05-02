from django.shortcuts import render, redirect
from Profile.models import Profile

def profile_page(request, user_id, user_name):
    try:
        profile = Profile.objects.get(user_id=user_id, user__username=user_name)
        context = {'profile': profile.user}
    except Profile.DoesNotExist:
        context = {'profile': None}
    return render(request, 'profile.html', context)