from django.contrib import admin
from login.views import loginaction
from signup.views import signupaction
from logout.views import logoutaction
from xevent.views import addEvent,showEvent,bookingSeat,bookSeat,bookSeat2,removeEvent,removeEvent2
from django.urls import path
from resetpass.views import resetpass
from ssbm import views
from dashboard.views import m_dashboard,m_dashboard2,manager_m_dashboard

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("booking/", bookingSeat, name='booking'),
    # path("login", views.login, name='login'),
    # path("signup", views.signup, name='signup'),
    path("login/", loginaction, name='login'),
    path("signup/", signupaction, name='signup'),
    path("logout/", logoutaction, name='logout'),
    path("prmtmsg/", views.prmtmsg, name='prmtmsg'),
    path("prmtmsg2/", views.prmtmsg2, name='prmtmsg2'),
    path("prmtmsg3/", views.prmtmsg3, name='prmtmsg3'),
    path("eprmtmsg/", views.eprmtmsg, name='eprmtmsg'),
    path("public/userMainPage/", views.userMainPage, name='userMainPage'),
    path("public/managerMainPage/", views.managerMainPage, name='managerMainPage'),
    path("public/managerProfile/", views.managerProfile, name='managerProfile'),
    path("resetPassword/", resetpass, name='resetPassword'),
    path("public/userProfile/", views.userProfile, name='userProfile'),
    path("public/userServices/u_mdashboard/", m_dashboard, name='u_mdashboard'),
    path("public/userServices/show_seatOnDashboard/<passvalue>", m_dashboard2, name='u_mdashboard2'),
    path("public/managerServices/manager_mdashboard/", manager_m_dashboard, name='manager_mdashboard'),
    path("public/userServices/bookYourSeat/<passvalue>", bookSeat, name="bookYourSeat"),
    path("public/userServices/bookYourSeat2/<passvalue>", bookSeat2, name="bookYourSeat2"),
    path("public/managerServices/managerMS/", views.managerMS, name="managerMS"),
    path("public/managerServices/addEvent/", addEvent, name="addEvent"),
    path("public/managerServices/showEvent/", showEvent, name="showEvent"),
    path("public/managerServices/removeEvent/", removeEvent, name="removeEvent"),
    path("public/managerServices/removeEvent2/<passvalue2>", removeEvent2, name="removeEvent2"),
    path("prmtemsg/", views.prmtemsg, name="prmtemsg"),
    path("userDashboard/", views.userDashboard, name="userDashboard"),
]