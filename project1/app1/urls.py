from django.contrib import admin
from django.urls import path,include
from . import views
from app1 import views
urlpatterns = [
    path('',views.HomePage,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('Profile',views.profile,name='profile'),
    path('settings',views.settings,name='settings'),
    path('contact',views.contact,name='contact'),

    ]