from django.shortcuts import render
from xevent.models import fetchEventRecord
import mysql.connector as mysql
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    if request.session.has_key('name'):
        name=request.session['name']
        cf=request.session['customer_fields']
        cf1="/public/"+cf+"MainPage"
        cf2="/public/"+cf+"Profile"
        return render(request,'about.html',{'name':name,'public':cf1,'publicprofile':cf2})
    else:
        return render(request,'login_page.html')
def services(request):
    if request.session.has_key('name'):
        name=request.session['name']
        cf=request.session['customer_fields']
        cf1="/public/"+cf+"MainPage"
        cf2="/public/"+cf+"Profile"
        return render(request,'services.html',{'name':name,'public':cf1,'publicprofile':cf2})
    else:
        return render(request,'login_page.html')
def booking(request):
    if request.session.has_key('name'):
        name=request.session['name']
        return render(request,'booking.html',{'name':name})
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
def userMainPage(request):
    if request.session.has_key('name'):
        name=request.session['name']
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
        return render(request,'public/userProfile.html',{'name':name})
    else:
        return render(request,'login_page.html')
def managerProfile(request):
    if request.session.has_key('name'):
        name=request.session['name']
        return render(request,'public/managerProfile.html',{'name':name})
    else:
        return render(request,'login_page.html')
def managerMS(request):
    if request.session.has_key('name'):
        name=request.session['name']
        return render(request,'public/managerServices/managerMS.html',{'name':name})
    else:
        return render(request,'login_page.html')
        
def removeEvent(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()
        return render(request,'public/managerServices/removeEvent.html',{'name':name,'eventdata':eventdata})
    else:
        return render(request,'login_page.html')

def removeEvent2(request,passvalue2):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()
        list1 = []
        list2 = []
        for i in eventdata:
            for j in range(1,i.ecol+1):
                list1.append(j)
            for k in range(1,i.erow+1):
                list2.append(k)
            i.ecol=list1
            i.erow=list2
            list2=[]
            list1=[]
            if i.ename == passvalue2:
                db = mysql.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "root",
                    database = "ssbm_db"
                )
                cursor = db.cursor()
                cursor.execute("delete from event_record where ename = %s",[passvalue2])
                db.commit()
                tablename1 = "event_"+passvalue2+"_seat"
                tablename2 = "event_"+passvalue2+"_user_booking"
                print(tablename1)
                q1 = "drop table "+tablename1
                q2 = "drop table "+tablename2
                cursor.execute(q1)
                cursor.execute(q2)
                db.commit()
                return render(request,'public/managerServices/removeEvent.html',{'name':name})
        return render(request,'public/managerServices/removeEvent.html',{'name':name,'eventdata':eventdata})
    else:
        return render(request,'login_page.html')

# def booking(request):
#     if request.session.has_key('name'):
#         name=request.session['name']
#         cf=request.session['customer_fields']
#         cf1="/public/"+cf+"MainPage"
#         cf2="/public/"+cf+"Profile"
#         return render(request,'booking.html',{'name':name,'public':cf1,'publicprofile':cf2})
#     else:
#         return render(request,'login_page.html')
# def profile(request,pro): 
#     if pro == 'user':
#         return render(request,'public/userProfile.html')
#     elif pro == 'manager':
#         return render(request,'public/managerProfile.html')
# def managerMainPage(request,pro):
#     return render(request,'public/managerMainPage.html')