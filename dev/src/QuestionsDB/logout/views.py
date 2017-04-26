from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_page(request):      
    previous_page = request.GET.get('redirect')
    logout(request)
    if previous_page is not None:
        return redirect(previous_page)
    return redirect('login_page')


