from django.contrib import admin
from django.urls import path
from ssbm import views
urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("booking", views.booking, name='booking'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),
]