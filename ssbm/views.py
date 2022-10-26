from django.shortcuts import render,HttpResponse

# return HttpResponse("this is from ssbm.views.about")

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
    # return HttpResponse("services.html")
def booking(request):
    return render(request,'bookings.html')
    # return HttpResponse("this is from ssbm.views.booking")
def login(request):
    return render(request,'login_page.html')
def signup(request):
    return render(request,'signup_page.html')
def prmtmsg(request):
    return render(request,'prompt_message.html')