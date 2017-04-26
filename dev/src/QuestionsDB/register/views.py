from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

class RegisterPage(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        email = request.POST['email']
        
        # if username = '':

        # user = User.objects.create_user(username=username, email=email, password=password)
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home_page')
        return render(request, 'register.html')

    def get(self, request):
        if not request.user.is_anonymous():
            if request.user is not None:
                return redirect('home_page')
        return render(request, 'register.html')

# def register_page(request):
#     if request.method == "GET":
#         if not request.user.is_anonymous():
#             if request.user is not None:
#                 return redirect('home_page')
#     return render(request, 'register.html')