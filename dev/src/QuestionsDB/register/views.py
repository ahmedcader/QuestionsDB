from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from Profile.models import Profile
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

class RegisterPage(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        email = request.POST['email']

        if not Profile.email_exists(email):
            if Profile.username_exists(username):
                print('cant create account. username already in use.')
        print('cant create account. email already in use.')

        return render(request, 'register.html')

    def get(self, request):
        if not request.user.is_anonymous():
            if request.user is not None:
                return redirect('home_page')
        return render(request, 'register.html')