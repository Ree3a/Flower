from django.shortcuts import render
from itertools import product
from django.shortcuts import redirect, render
from . import forms, models
from .forms import ProductForm
from django.contrib.auth import  authenticate
from django.contrib import messages
# from .models import ProductForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.


@login_required(login_url='admin')
def admin_products_view(request):
    products=models.Product.objects.all()
    return render(request,'adminControl/admin_product.html',{'products':products})

# admin add product by clicking on floating button
@login_required(login_url='admin')
def admin_add_product(request):
    print(request.FILES)
    if request.method=="POST":
        products=ProductForm(request.POST,request.FILES)
        products.save()
        return redirect ("adminControl/adminlogin.html")
    else:
        products=ProductForm()
    return render (request,"adminControl/addproduct.html",{'products':products})