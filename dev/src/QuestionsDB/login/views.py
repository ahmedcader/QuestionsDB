from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from datetime import datetime
from Profile.models import Profile


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    previous_page = request.GET.get('redirect')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(previous_page)
    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect(previous_page)
    return render(request, 'login.html')