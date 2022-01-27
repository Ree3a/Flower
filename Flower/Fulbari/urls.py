from unicodedata import name
from django.urls import path
from Fulbari import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login/', views.login, name='login'),
    path("register/",views.register, name='register'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('logout', views.logout, name="logout")
]
