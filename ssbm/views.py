from django.shortcuts import render,HttpResponse

# return HttpResponse("this is from ssbm.views.about")

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return HttpResponse("this is from ssbm.views.services")
def booking(request):
    return HttpResponse("this is from ssbm.views.booking")
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')