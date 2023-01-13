from django.shortcuts import render
from xevent.models import fetchEventRecord,fetchSeatRecord
from signup.models import userData
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    if request.session.has_key('name'):
        name=request.session['name']
        profile=request.session['profile']

        mainPagelink="public/"+profile+"MainPage"
        profilelink="public/"+profile+"Profile/"

        if profile=="user":
            
            navlink1="/booking/"
            navlink1_value="Booking"
            Dashboard="/public/userServices/u_mdashboard/"

            return render(request,'about.html',{'name':name,'profile':profile,'mainPagelink':mainPagelink,'navlink1':navlink1,'navlink1_value':navlink1_value,'Dashboard':Dashboard,'profilelink':profilelink})
        else:

            navlink1="/public/managerServices/managerMS/"
            navlink1_value="Services"
            Dashboard="/public/managerServices/manager_mdashboard/"

            return render(request,'about.html',{'name':name,'profile':profile,'mainPagelink':mainPagelink,'navlink1':navlink1,'navlink1_value':navlink1_value,'Dashboard':Dashboard,'profilelink':profilelink})
        # return render(request,'about.html',{'name':name,'profile':profile,'navlink1':navlink1,'profile2':profile2})
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
        eventdata = fetchEventRecord.objects.all()
        return render(request,'public/userMainPage.html',{'name':name,'event':eventdata})
    else:
        return render(request,'login_page.html')
def managerMainPage(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()
        # image from unsplash.com
        
        for i in range(len(eventdata)):
            modified_ename = eventdata[i].ename
            modified_ename = modified_ename.replace(" ", "-")

        return render(request,'public/managerMainPage.html',{'name':name,'event':eventdata,'imgLink':modified_ename})
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