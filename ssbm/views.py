from django.shortcuts import render

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
        return render(request,'public/managerServices/removeEvent.html',{'name':name})
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