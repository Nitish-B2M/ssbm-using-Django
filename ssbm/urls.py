from django.contrib import admin
from login.views import loginaction
from signup.views import signupaction
from xevent.views import addEvent,showEvent
from django.urls import path
from resetpass.views import resetpass
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
    path("prmtmsg2/", views.prmtmsg2, name='prmtmsg2'),
    path("public/userMainPage/", views.userMainPage, name='userMainPage'),
    path("public/managerMainPage/", views.managerMainPage, name='managerMainPage'),
    path("public/userProfile/", views.userProfile, name='userProfile'),
    path("public/managerProfile/", views.managerProfile, name='managerProfile'),
    path("resetPassword/", resetpass, name='resetPassword'),
    path("booking/", views.booking, name="booking"),
    path("public/managerServices/managerMS/", views.managerMS, name="managerMS"),
    path("public/managerServices/addEvent/", addEvent, name="addEvent"),
    path("public/managerServices/showEvent/", showEvent, name="showEvent"),
    path("public/managerServices/removeEvent/", views.removeEvent, name="removeEvent"),
    path("prmtemsg/", views.prmtemsg, name="prmtemsg"),

    # path("public/managerMainPage/<int:pro>/", views.managerMainPage, name='managerMainPage'),
]