
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Product import views



urlpatterns = [

     path('admin-products', views.admin_products_view,name='admin-products'),
     # path('addproduct', views.admin_add_product, name='addproduct'),
]