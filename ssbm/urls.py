from django.contrib import admin
from login.views import loginaction
from signup.views import signupaction
from django.urls import path
from ssbm import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("booking", views.booking, name='booking'),
    # path("login", views.login, name='login'),
    # path("signup", views.signup, name='signup'),
    path("login/", loginaction, name='login'),
    path("signup/", signupaction, name='signup'),
    path("prmtmsg/", views.prmtmsg, name='prmtmsg'),
]