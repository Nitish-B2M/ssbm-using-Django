from django.shortcuts import render
from xevent.models import fetchSeatRecord,fetchEventRecord,fetchUserRecord

# Create your views here.
def m_dashboard(request):
    if request.session.has_key('name'):
        name = request.session['name']
        seatrecord = fetchSeatRecord.objects.all()
        eventrecord = fetchEventRecord.objects.all()
        userrecord = fetchUserRecord.objects.all()
        page_exist = 0
        list1 = []
        for i in userrecord:
            for j in eventrecord:
                if i.username == name and i.eventname == j.ename:
                    page_exist = 1
                    list1.append(j)
        list1 = list(set(list1))
        return render(request, 'public/userServices/Mdashboard.html', {'seatrecord': seatrecord, 'eventrecord': list1, 'name': name, 'userrecord': userrecord, 'page_exist': page_exist})

def m_dashboard2(request,passvalue):
    if request.session.has_key('name'):
        name = request.session['name']
        seatrecord = fetchSeatRecord.objects.all()
        eventrecord = fetchEventRecord.objects.all()
        userBookedRecord = fetchUserRecord.objects.all()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list1_data=""
        cond_count = 0
        for i in eventrecord:
            if i.ename == passvalue:
                cond_count = 1
                list1_data=i

                list1=[]
                list2=[]
                for j in range(1,i.ecol+1):
                    list1.append(j)
                for k in range(1,i.erow+1):
                    list2.append(k)
                i.ecol=list1
                i.erow=list2
                list1=[]
                list2=[]

        for j in seatrecord:
            if j.eventname == passvalue:
                list2.append(j)

        for k in userBookedRecord:
            if k.eventname == passvalue:
                list3.append(k)

        userBookedRecord_price = 0
        for k in userBookedRecord:
            if k.eventname == passvalue and k.username == name:
                userBookedRecord_price += k.seattotalprice
                list4.append(k.userseat)

        for n in list4:
            n=n.split(',')
            if len(n) >= 1:
                for m in n:
                    list5.append(m)
        for x in list2:
            for y in list5:
                if x.seatname == y:
                    x.seatstatus = 2
                    
        # print(list5)
        if cond_count == 1:
            return render(request, 'public/userServices/show_seatOnDashboard.html', {'name' : name, 'eventdata': list1_data, 'seatdata': list2, 'userBookedRecord': list3, 'userBookedSeat': list5, 'userBookedRecord_price': userBookedRecord_price})
        else:
            return render(request,'public/userServices/Mdashboard.html',{'name':name,'bseat':eventrecord,'page':''})
    else:
        return render(request,'login_page.html')

def manager_m_dashboard(request):
    if request.session.has_key('name'):
        name = request.session['name']
        seatrecord = fetchSeatRecord.objects.all()
        seatrecord2 = fetchSeatRecord.objects.all()
        eventrecord = fetchEventRecord.objects.all()
        userrecord = fetchUserRecord.objects.all()
        if eventrecord:
            page_exist = 1
        
        for i in seatrecord:
            if i.seatstatus == 1:
                seatrecord2 = seatrecord2.exclude(seatname=i.seatname)
        

        # seatleft = userrecord.count() - userrecord2.count()
        # print(seatleft)
        return render(request, 'public/managerServices/Manager_MDashboard.html', {'seatrecord': seatrecord, 'eventrecord': eventrecord, 'name': name, 'userrecord': userrecord, 'page_exist': page_exist, })