from django.shortcuts import render,redirect
from xevent.models import fetchEventRecord,fetchSeatRecord,fetchUserRecord,fetchFeedbackRecord
import datetime

# add Event Function
def addEvent(request):
    if request.session.has_key('name'):
        name=request.session['name']
        global bname, borgname, bdate, bvenue, bstime, betime, bdescription
        if request.method == 'POST':
            be = request.POST
            bname = be['leventname']
            borgname = be['leventorganization']
            bdate = be['leventdate']
            bvenue = be['leventvenue']
            bstime = be['leventstarttime']
            betime = be['leventendtime']
            bdescription = be['leventdesc']
            bcol = be['leventcol']
            brow = be['leventrow']
            bprice = be['lprice']
            if bname == ' ' or borgname == ' ' or bdate == ' ' or bvenue == ' ' or bstime == ' ' or betime == ' ' or bdescription == ' ' or bcol == ' ' or brow == ' ':
                return render(request,'public/managerServices/addEvent.html',{'error1':'Please fill all the fields','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            elif bstime > betime:
                return render(request,'public/managerServices/addEvent.html',{'error2':'Start time cannot be greater than end time','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            elif bstime == betime:
                return render(request,'public/managerServices/addEvent.html',{'error3':'Start time cannot be equal to end time','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            elif bdate == datetime.datetime.today():
                if bstime < datetime.datetime.now().time():
                    return render(request,'public/managerServices/addEvent.html',{'error5':'Start time cannot be less than current time','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            elif bprice == 0:
                return render(request,'public/managerServices/addEvent.html',{'error4':'Price cannot be zero','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            else:
            
                isEventPresent = fetchEventRecord.objects.filter(ename=bname, eorganization=borgname ,edate=bdate,evenue=bvenue,estarttime=bstime,eendtime=betime,edesc=bdescription,seatprice=bprice)
                
                eventCount = fetchEventRecord.objects.all().count()
                if eventCount == 0:
                    bid = 1
                else:
                    bid = fetchEventRecord.objects.all().last().id + 1

                if isEventPresent:
                    return render(request,'public/managerServices/addEvent.html',{'error6':'Event already exists','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
                else:

                    temp_name=bname.replace(" ","_")

                    addingEvent = fetchEventRecord(id=bid,ename=bname, eorganization=borgname, edate=bdate, evenue=bvenue, estarttime=bstime, eendtime=betime, edesc=bdescription, ecol=bcol, erow=brow, seatprice=bprice)
                    addingEvent.save()

                    counter = 1
                    for i in range(1,int(brow)+1):
                        for j in range(1,int(bcol)+1):
                            seatname="s"+str(i)+"_"+str(j)
                            addingSeat = fetchSeatRecord(seatname=seatname,seatstatus=0,no_row=brow,no_col=bcol,row_count=counter,eventname=bname)
                            addingSeat.save()
                            
                        counter = counter + 1
                    return render(request,'public/managerServices/managerMS.html',{'success':'Event added successfully','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription,'bcol':bcol,'brow':brow})
        else:
            return render(request,'public/managerServices/addEvent.html',{'name':name})
    else:
        return render(request,'login_page.html')

# show Event List in Manager Services
# Path: ssbm-using-Django/xevent/views.py
global eventdata
def showEvent(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()                
        return render(request,'public/managerServices/showEvent.html',{'event':eventdata,'name':name,'img':"https://source.unsplash.com/250x280/?stadium",'img2':"https://source.unsplash.com/300x250/?stadium"})
    else:
        return render(request,'login_page.html')

# show Event List in Booking.html 
def bookingSeat(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()
        boxcolor=['#F5CBBF','#FFA500','#FFFF00','#88B2A9','#F3AEFA','#D98859','#EE82EE','#DEE6AC','#7B8387','#B4C6D2','#69A488','#A49969','#929292','#BFB393','#62EC4D','#BFA0A5']
        return render(request,'booking.html',{'bseat':eventdata,'name':name,'img':"https://source.unsplash.com/250x250/?stadium",'boxcolor':boxcolor})
    else:
        return render(request,'login_page.html')

# show particular Event details and seat slot in User Services/bookSeat.html
def bookSeat(request,passvalue):
    if request.session.has_key('name'):
        name=request.session['name']
        # logic for booking seat
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
            if i.ename == passvalue:
                ename=i.ename 
                # passvalue = passvalue.replace(" ","_")
                seatdata = fetchSeatRecord.objects.all()
                l1 = []
                for j in seatdata:
                    if j.eventname == passvalue:
                        l1.append(j)
                return render(request,'public/userServices/bookSeat.html',{'bseat':i,'name':name,'page':'page_exist','ename':ename,'seatdata':l1,'img':"https://source.unsplash.com/250x250/?stadium"})
            else:
                pass
        return render(request,'public/userServices/bookSeat.html',{'name':name,'bseat':eventdata,'page':''})
    else:
        return render(request,'login_page.html')

# booking seat by user backend
def bookSeat2(request,passvalue):
    if request.session.has_key('name'):
        name=request.session['name']
        email=request.session['email']
        # insert data into database event_xx_user_booking
        sseat = []
        if request.method == 'POST':
            bseat = request.POST.getlist('sseat')
            for i in bseat:
                sseat.append(i)
        snoseat = len(sseat)
        if name == ' ' or email == ' ' or sseat == ' ' or snoseat == ' ':
            return render(request,'/public/userServices/bookSeat.html',{'error1':'Please fill all the fields'})
        else:

            isEventExist = fetchEventRecord.objects.filter(ename=passvalue)
            if isEventExist:
                seatprice = isEventExist[0].seatprice
                stotalprice = snoseat * seatprice
                str_seat = ','.join(sseat)
                eventSeatUserEntries = fetchUserRecord(username=name, useremail=email, userseat=str_seat, no_seat=snoseat, seattotalprice=stotalprice, eventname=passvalue)
                eventSeatUserEntries.save()
                for i in sseat:
                    updatingSeatStatus = fetchSeatRecord.objects.filter(seatname=i,eventname=passvalue).update(seatstatus=1)

                            # return render(request,'public/managerServices/showEvent.html',{'error2':'Seat already booked','name':name,'page':'page_exist','ename':passvalue})
                return render(request,'public/userMainPage.html',{'success':'Seat booked successfully','name':name,'page':'page_exist','ename':passvalue})
            else:
                return render(request,'booking.html',{'error3':'Seat does not exist','name':name})

# show Event List in Manager Services for remove event
def removeEvent(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()
        return render(request,'public/managerServices/removeEvent.html',{'name':name,'eventdata':eventdata})
    else:
        return render(request,'login_page.html')

# remove Event from database
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
            # passvalue2 = passvalue2.replace(" ","_")
            if request.method == 'POST':
                ename = request.POST['ename']
                if i.ename == passvalue2:

                    # deleting events from database
                    isEventExist = fetchEventRecord.objects.filter(ename=ename)
                    if isEventExist:
                        isEventExist.delete()
                    isSeatExist = fetchSeatRecord.objects.filter(eventname=ename)
                    if isSeatExist:
                        isSeatExist.delete()
                    isUserBookingExist = fetchUserRecord.objects.filter(eventname=ename)
                    if isUserBookingExist:
                        isUserBookingExist.delete()
                    return render(request,'prompt_message3.html',{'name':name})
                else:
                    pass
                
        return redirect('/managerServices/showEvent/')
    else:
        return render(request,'login_page.html')
