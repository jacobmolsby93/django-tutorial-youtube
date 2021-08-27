from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# django function named login, so our function needs to be different.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # REMOVE THIS \/
        print(username, password)
        user = authenticate(request, username=username, password=password)
        # if user is none, this function will not work, | user none == not existing
        if user is None:
            context = {'error': 'invalid username or password'}
            return render(request, 'accounts/login.html', context)            
        print(user)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout.html', {})

def register_view(request):
    return render(request, 'accounts/register.html', {})