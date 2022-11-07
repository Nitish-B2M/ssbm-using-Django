from django.shortcuts import render,HttpResponse
from xevent.models import fetchEventRecord,fetchSeatRecord
import mysql.connector as mysql
import datetime

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
                db = mysql.connect(
                    host="localhost",
                    user="root",
                    passwd="root",
                    database="ssbm_db"
                )
                cursor = db.cursor()
                cursor.execute("SELECT * FROM event_record WHERE ename = %s AND edate = %s AND evenue = %s AND estarttime = %s AND eendtime = %s AND edesc = %s AND seatprice = %s", (bname, bdate, bvenue, bstime, betime, bdescription, bprice))
                event = cursor.fetchone()
                cursor.execute("select id from event_record")
                getdata=cursor.fetchall()
                if len(getdata) == 0:
                    bid = 1
                else:
                    bid = getdata[-1][0] + 1
                if event:
                    return render(request,'public/managerServices/addEvent.html',{'error6':'Event already exists','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
                else:
                    temp_name=bname.replace(" ","_")
                    event_seat_name="event_"+temp_name+"_seat"
                    event_user_booking_name="event_"+temp_name+"_user_booking"
                    cursor.execute("create table if not exists "+event_seat_name+" (seat_srno int primary key auto_increment, seatname varchar(20), seatstatus int, no_row int not null, no_col int not null, row_count int not null)")
                    cursor.execute("create table if not exists "+event_user_booking_name+" (user_srno int primary key auto_increment, username varchar(50), useremail varchar(50), userseat varchar(50), no_seat int not null, seattotalprice int not null)")
                    db.commit()

                    cursor.execute("INSERT INTO event_record(id,ename, eorganization, edate, evenue, estarttime, eendtime, edesc, ecol, erow, seatprice) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (bid,bname, borgname, bdate, bvenue, bstime, betime, bdescription, bcol, brow, bprice))
                    counter = 1
                    for i in range(1,int(bcol)+1):
                        for j in range(1,int(brow)+1):
                            seatname="seat_"+str(i)+"_"+str(j)
                            cursor.execute("INSERT INTO "+event_seat_name+" (seatname, seatstatus, no_row, no_col, row_count) VALUES (%s, %s, %s, %s, %s)", (seatname,0,brow,bcol,counter))
                        counter = counter + 1
                    db.commit()
                    return render(request,'public/managerServices/managerMS.html',{'success':'Event added successfully','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription,'bcol':bcol,'brow':brow})
        else:
            return render(request,'public/managerServices/addEvent.html',{'name':name})
    else:
        return render(request,'login_page.html')

# showEvent
# Path: ssbm-using-Django/xevent/views.py
global eventdata
def showEvent(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()                  
        return render(request,'public/managerServices/showEvent.html',{'event':eventdata,'name':name,'img':"https://source.unsplash.com/300x250/?stadium",'img2':"https://source.unsplash.com/300x250/?stadium"})
    else:
        return render(request,'login_page.html')

def bookingSeat(request):
    if request.session.has_key('name'):
        name=request.session['name']
        eventdata = fetchEventRecord.objects.all()
        boxcolor = {'1':'#F5CBBF','2':'#FFA500','3':'#FFFF00','4':'#88B2A9','5':'#F3AEFA','6':'#D98859','7':'#EE82EE','8':'#DEE6AC','9':'#698DA4','10':'#7B8387','11':'#B4C6D2','12':'#69A488','13':'#A49969','14':'#929292','15':'#BFB393','16':'#62EC4D','17':'#BFA0A5'}
        return render(request,'booking.html',{'bseat':eventdata,'name':name,'img':"https://source.unsplash.com/250x250/?stadium",'boxcolor':boxcolor})
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
                seatdata = fetchSeatRecord.objects.all()
                
                request.session['ename'] = i.ename
                return render(request,'public/userServices/bookSeat.html',{'bseat':i,'name':name,'page':'page_exist','ename':i.ename,'seatdata':seatdata,'img':"https://source.unsplash.com/250x250/?stadium"})
            else:
                pass
        return render(request,'public/userServices/bookSeat.html',{'name':name,'bseat':eventdata,'page':''})
    else:
        return render(request,'login_page.html')

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
            return render(request,'booking.html',{'error1':'Please fill all the fields'})
        else:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="ssbm_db"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM event_record WHERE ename = %s", (passvalue,))
            event = cursor.fetchone()
            if event:
                seatprice = event[10]
                stotalprice = snoseat * seatprice
                temp_name=passvalue.replace(" ","_")
                event_seat_name="event_"+temp_name+"_seat"
                event_user_booking_name="event_"+temp_name+"_user_booking"
                for i in sseat:
                    cursor.execute("SELECT * FROM "+event_seat_name+" WHERE seatname = %s", (i,))
                    seat = cursor.fetchone()
                    if seat:
                        if seat[2] == 0:
                            cursor.execute("INSERT INTO "+event_user_booking_name+" (username, useremail, userseat, no_seat, seattotalprice) VALUES (%s, %s, %s, %s, %s)", (name, email, i, snoseat, stotalprice))
                            cursor.execute("UPDATE "+event_seat_name+" SET seatstatus = 1 WHERE seatname = %s", (i,))
                            db.commit()
                            return render(request,'public/managerServices/showEvent.html',{'success':'Seat booked successfully','name':name,'page':'page_exist','ename':passvalue})
                        else:
                            return render(request,'public/managerServices/showEvent.html',{'error2':'Seat already booked','name':name,'page':'page_exist','ename':passvalue})
                else:
                    return render(request,'booking.html',{'error3':'Seat does not exist','name':name})
