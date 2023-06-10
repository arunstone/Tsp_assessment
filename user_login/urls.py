from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.LandingPage,name="LandingPage"),
    path('RegisterPage',views.RegisterPage,name='RegisterPage'),
    path('LoginPage',views.LoginPage,name='LoginPage'),

]