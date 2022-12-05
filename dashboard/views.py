from django.shortcuts import render
from xevent.models import fetchSeatRecord,fetchEventRecord,fetchUserRecord

# Create your views here.
def m_dashboard(request):
    if request.session.has_key('name'):
        name = request.session['name']
        seatrecord = fetchSeatRecord.objects.all()
        eventrecord = fetchEventRecord.objects.all()
        userrecord = fetchUserRecord.objects.all()
        return render(request, 'public/userServices/Mdashboard.html', {'seatrecord': seatrecord, 'eventrecord': eventrecord, 'name': name, 'userrecord': userrecord})

def m_dashboard2(request,passvalue):
    if request.session.has_key('name'):
        name = request.session['name']
        seatrecord = fetchSeatRecord.objects.all()
        eventrecord = fetchEventRecord.objects.all()
        userrecord = fetchUserRecord.objects.all()
        list1 = []
        list2 = []
        for i in eventrecord:
            for j in range(1,i.ecol+1):
                list1.append(j)
            for k in range(1,i.erow+1):
                list2.append(k)
            i.ecol=list1
            i.erow=list2
            list2=[]
            list1=[]
            if i.ename == passvalue:
                ename=i.ename 
                seatdata = fetchSeatRecord.objects.all()
                l1 = []
                for j in seatdata:
                    if j.eventname == passvalue:
                        l1.append(j)
                getuserdata = fetchUserRecord.objects.get(username=name)
                getprice = getuserdata.seattotalprice
                return render(request,'public/userServices/show_seatOnDashboard.html',{'bseat':i,'name':name,'page':'page_exist','ename':ename,'seatdata':l1,'img':"https://source.unsplash.com/250x250/?stadium",'userrecord':userrecord,'getprice':getprice})
            else:
                pass
        return render(request,'public/userServices/Mdashboard.html',{'name':name,'bseat':eventrecord,'page':''})
    else:
        return render(request,'login_page.html')