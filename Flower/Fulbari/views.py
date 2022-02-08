# from itertools import product
from django.shortcuts import redirect, render
from .forms import *
from django.forms import forms, models
# from .forms import CustomerForm
from django.contrib.auth import  authenticate
from django.contrib import messages
# from Fulbari.models import Product

from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

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


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email'] 
        message =request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            # settings.EMAIL_HOST_USER,
            #           ['riyastha406@mail.com'],
            ['riyastha406@gmail.com' ], #To email
            # fail_silently= True,
        )   
        return render(request, 'pages/contact.html', {'message_name': message_name}) 

    else:
        return render(request, 'pages/contact.html' , {})     

@login_required
def afterlogin_view(request):
    if request.user.is_superuser:
        return redirect('admindashboard')
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')

@login_required(login_url='admin')
def admindashboard_view(request):
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request, 'adminControl/admindashboard.html')
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')



#admin view the product 

