from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    authenticated = authenticate(username=username, password=password)
    if authenticated:
        login(request, authenticated)
        request.session['username'] = authenticated.username
        return redirect('/')
    else:
        pass


def log_out(request):
    logout(request)
    return redirect('/')
