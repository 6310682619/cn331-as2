from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('registrar:index'))
        else:
            return render(request, 'user/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'user/login.html', {
        'message': 'Logged out'
    })

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user:login'))
    return render(request, 'registrar/index.html')

def user(request):
    return render(request, 'user/index.html')