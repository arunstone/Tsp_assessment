from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def LandingPage(request):
    return render(request,'user_login/LandingPage.html')
def RegisterPage(request):
    if request.method=='POST':
        print("hello")
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['mobile']
        password=request.POST['password']
        user1=user_login.objects.create(name=name,email=email,number=number,password=password)
        user1.save()
    return render(request,'user_login/register.html')
def LoginPage(request):
    if request.method=='POST':
        password=request.POST['password']
        email=request.POST['email']
        try:
            feature=user_login.objects.all()
            feature=user_login.POST.get(email=email) 
        except user_login.DoesNotExist:
            feature=None
        if feature is not None and feature.password==password:
            return HttpResponse('succesfull registered')
        else:
            return HttpResponse('recheck the datra')
    else:
        return HttpResponse('sorry')

