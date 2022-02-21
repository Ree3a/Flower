# from itertools import product
from django.shortcuts import redirect, render
# from .forms import *
from .import forms, models
# from .forms import CustomerForm
from django.contrib.auth import  authenticate , get_user_model
from django.shortcuts import get_object_or_404
from django.contrib import messages
from Product.models import Product,Orders
from Fulbari.models import Blogs
from .forms import BlogForm
from django.http import HttpResponseRedirect,HttpResponse
from Fulbari.forms import UserForm
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'pages/homepage.html')

def about(request):
    return render(request,'pages/about.html')

def product(request):
    products=Product.objects.all()
    return render(request,'product/product.html',{'products':products,})    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, "You are now logged in")    
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'pages/login.html')  


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        auth.login(request, user)
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

        usercount =User.objects.all().filter(is_superuser=False).count()
        productcount =Product.objects.all().count()
        bookcount =Orders.objects.all().count()
        data ={
            'usercount': usercount,
            'productcount':productcount,
            'bookcount':bookcount,
        }
        return render(request, 'adminControl/admindashboard.html',data)
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')


def blogform(request):
    print(request.FILES)
    if request.method=="POST":
        blogs=BlogForm(request.POST,request.FILES)
        blogs.save()
        return redirect ("blog")
    else:
        blogs=BlogForm()
    return render (request,"pages/blog_form.html",{'blogs':blogs})

def allblog(request):
    blogs=Blogs.objects.all()
    paginator = Paginator(blogs, 1)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'blogs': paged_product,
    }
    return render (request,"adminControl/allblogs.html",data)


def showblog(request):
    blogs=Blogs.objects.all()

    return render (request,"pages/blog.html",{'blogs':blogs})


def blog_detail(request, id):
    single_blog = get_object_or_404(Blogs, pk=id)

    data = {
        'single_blog': single_blog,
    }

    return render(request, 'pages/blog_single.html', data)    


@login_required(login_url='admin')
def delete_blog_view(request,pk):
    blogs=Blogs.objects.get(blog_id=pk)
    blogs.delete()
    return redirect('blog')  

@login_required(login_url='admin')
def update_blog_view(request,pk):
    blogs=models.Blogs.objects.get(blog_id=pk)
    blogform=forms.BlogForm(instance=blogs)
    if request.method=='POST':
        blogform=forms.BlogForm(request.POST,request.FILES,instance=blogs)
        if blogform.is_valid():
            blogform.save()
            return redirect('allblog')
    return render(request,'pages/update_blog.html',{'blogform':blogform,'blogs':blogs})      


@login_required(login_url='adminlogin')
def view_customer(request):
    User = get_user_model()
    users=User.objects.all().order_by('username').filter(is_superuser=False)
    paginator = Paginator(users, 1)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'users': paged_product,
    }
    return render(request,'admincontrol/view_customer.html',data)


# @login_required(login_url='admin')
# def delete_customer_view(request,pk):
#     users=User.objects.get(id=pk)
#     users.delete()
#     return redirect('view-customer')    


def profile(request):
     return render(request, 'pages/profile.html')

@login_required(login_url='login')
def edit_profile_view(request):
    user = User.objects.get(id=request.user.id)
    userForm = UserForm(instance=user)
    mydict = {
        'userForm': userForm,
        'user': user
    }
    if request.method == 'POST':
        userForm = UserForm(request.POST, request.FILES, instance=user)
        if userForm.is_valid():
            user.set_password(user.password)
            userForm.save()

            return HttpResponseRedirect('dashboard')

    return render(request, 'pages/edit_profile.html', context=mydict)      


def profile(request):
     return render(request, 'pages/profile.html')    


    