from django.shortcuts import render
from xevent.models import fetchEventRecord,fetchSeatRecord
from signup.models import userData
import mysql.connector as mysql
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    if request.session.has_key('name'):
        name=request.session['name']
        profile=request.session['profile']
        profile1="public/"+profile+"MainPage"
        navbar_op3_user="/booking/"
        navbar_op3_value="Booking"
        navbar_op3_manager="/public/managerServices/managerMS/"
        navbar_op3_value_manager="Services"
        userDashboard="/public/userServices/u_mdashboard/"
        userDashboard_value="Dashboard"
        if profile=="user":
            return render(request,'about.html',{'name':name,'profile':profile,'profile1':profile1,'navbar_op3':navbar_op3_user,'navbar_op3_value':navbar_op3_value,'userDashboard':userDashboard,'userDashboard_value':userDashboard_value})
        else:
            return render(request,'about.html',{'name':name,'profile':profile,'profile1':profile1,'navbar_op3':navbar_op3_manager,'navbar_op3_value':navbar_op3_value_manager})
        # return render(request,'about.html',{'name':name,'profile':profile,'profile1':profile1,'profile2':profile2})
    else:
        return render(request,'login_page.html')
def services(request):
    if request.session.has_key('name'):
        name=request.session['name']
        return render(request,'services.html',{'name':name})
    else:
        return render(request,'login_page.html')
def booking(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata=fetchEventRecord.objects.all()
        return render(request,'booking.html',{'name':name,'event':eventdata})
    else:
        return render(request,'login_page.html')
def prmtmsg(request):
    return render(request,'prompt_message.html')
def prmtemsg(request):
    return render(request,'prompt_emessage.html')
def prmtmsg2(request):
    return render(request,'prompt_message2.html')
def prmtmsg3(request):
    return render(request,'prompt_message3.html')
def eprmtmsg(request):
    return render(request,'prompt_emessage.html')
def userMainPage(request):
    if request.session.has_key('name'):
        name=request.session['name']
        profile=request.session['profile']
        return render(request,'public/userMainPage.html',{'name':name})
    else:
        return render(request,'login_page.html')
def managerMainPage(request):
    if request.session.has_key('name'):
        name=request.session['name']
        return render(request,'public/managerMainPage.html',{'name':name})
    else:
        return render(request,'login_page.html')
def userProfile(request):
    if request.session.has_key('name'):
        name=request.session['name']
        userrecord=userData.objects.get(name=name)
        return render(request,'public/userProfile.html',{'name':name,'user':userrecord})
    else:
        return render(request,'login_page.html')
def managerProfile(request):
    if request.session.has_key('name'):
        name=request.session['name']
        userrecord=userData.objects.get(name=name)
        return render(request,'public/managerProfile.html',{'name':name,'user':userrecord})
    else:
        return render(request,'login_page.html')
def managerMS(request):
    if request.session.has_key('name'):
        name=request.session['name']
        return render(request,'public/managerServices/managerMS.html',{'name':name})
    else:
        return render(request,'login_page.html')

def userDashboard(request):
    if request.session.has_key('name'):
        name=request.session['name']
        return render(request,'public/userDashboard.html',{'name':name})
    else:
        return render(request,'login_page.html')