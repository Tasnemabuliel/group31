from contextlib import _RedirectStream
from email import message
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
#from models import *
from .forms import createUserForm

def home(request):
    return render(request,'app1/index.html')


def signup(request):
    form=UserCreationForm()
    if request.method=="POST":
         form=createUserForm(request.POST)
         if form.is_valid():
            form.save()
            user=form.cleaned_data.get('userame')
            messages.success(request,'Account was created for'+user)
            return redirect('signin')

    context={'form':form}
    return render(request,'app1/signup.html',context)

def signin(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('HomePage')


    return render(request,'app1/signin.html')

def signout(request):
    logout(request)
    return redirect('home')

def HomePage(request):
    return render(request,'app1/HomePage.html')  


def profile(request):
    return render(request,'app1/profile.html')


def settings(request):
    return render(request,'app1/settings.html')
