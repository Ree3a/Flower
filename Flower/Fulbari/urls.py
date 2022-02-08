from unicodedata import name
from django.urls import path
from Fulbari import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login/', views.login, name='login'),
    path("register/",views.register, name='register'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('contact',views.contact, name='contact'),
    path('logout', views.logout, name="logout"),

    # Most important functon
    path('afterlogin', views.afterlogin_view, name="afterlogin"),
    path('admindashboard', views.admindashboard_view, name="admindashboard"),
    #  path('admin-products', views.admin_products_view,name='admin-products'),
]

