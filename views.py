from contextlib import _RedirectStream
from email import message
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'app1/index.html')


def signup(request):
    
    return render(request,'app1/signup.html')

def signin(request):
    return render(request,'app1/signin.html')

def signout(request):
    pass
def HomePage(request):
    return render(request,'app1/HomePage.html')
def windowfavorite(request):
    return render(request,'app1/windowfavorite.http')