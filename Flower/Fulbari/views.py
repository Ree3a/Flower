from django.shortcuts import redirect, render
from .forms import *
from django.forms import forms
from .forms import CustomerForm
from django.contrib.auth import  authenticate
from django.contrib import messages

from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/homepage.html')

def about(request):
    return render(request,'pages/about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'pages/login.html')  


def register(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
                            username=username,
                            email=email,
                            password=password)

        user.save()
        return redirect('login')
    else:
        return render(request, 'pages/register.html')    

@login_required(login_url='login')
def dashboard(request):
    return render(request,'pages/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are successfully logged out.')
        return redirect('login') 
    return redirect('home')
