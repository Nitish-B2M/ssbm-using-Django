from django.shortcuts import render
from xevent.models import fetchEventRecord
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
            if bname == ' ' or borgname == ' ' or bdate == ' ' or bvenue == ' ' or bstime == ' ' or betime == ' ' or bdescription == ' ':
                return render(request,'public/managerServices/addEvent.html',{'error1':'Please fill all the fields','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            elif bstime > betime:
                return render(request,'public/managerServices/addEvent.html',{'error2':'Start time cannot be greater than end time','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            elif bstime == betime:
                return render(request,'public/managerServices/addEvent.html',{'error3':'Start time cannot be equal to end time','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            # elif bdate < datetime.datetime.today().date():
            #     return render(request,'public/managerServices/addEvent.html',{'error4':'Date cannot be less than today','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            elif bdate == datetime.datetime.today():
                if bstime < datetime.datetime.now().time():
                    return render(request,'public/managerServices/addEvent.html',{'error5':'Start time cannot be less than current time','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
            else:
                print(bname, borgname, bdate, bvenue, bstime, betime, bdescription)
                db = mysql.connect(
                    host="localhost",
                    user="root",
                    passwd="root",
                    database="event_db"
                )
                cursor = db.cursor()
                cursor.execute("SELECT * FROM event_record WHERE ename = %s AND edate = %s AND evenue = %s AND estarttime = %s AND eendtime = %s AND edesc = %s", (bname, bdate, bvenue, bstime, betime, bdescription))
                event = cursor.fetchone()
                if event:
                    return render(request,'public/managerServices/addEvent.html',{'error6':'Event already exists','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
                else:
                    cursor.execute("INSERT INTO event_record(ename, eorganization, edate, evenue, estarttime, eendtime, edesc) VALUES (%s, %s, %s, %s, %s, %s, %s)", (bname, borgname, bdate, bvenue, bstime, betime, bdescription))
                    db.commit()
                    return render(request,'public/managerServices/showEvent.html',{'success':'Event added successfully','name':name,'bname':bname,'borgname':borgname,'bdate':bdate,'bvenue':bvenue,'bstime':bstime,'betime':betime,'bdescription':bdescription})
        else:
            return render(request,'public/managerServices/addEvent.html',{'name':name})
    else:
        return render(request,'login_page.html')
# showEvent
# Path: ssbm-using-Django/xevent/views.py
def showEvent(request):
    if request.session.has_key('name'):
        name=request.session['name']
        # db = mysql.connect(
        #     host="localhost",
        #     user="root",
        #     passwd="root",
        #     database="event_db"
        # )
        # cursor = db.cursor()
        # cursor.execute("SELECT * FROM event_record")
        # eventdata = cursor.fetchall()
        # print(eventdata[0][1])
        # fetcheddata = {'name':[],'org':[]}
        # for x in eventdata:
        #     fetcheddata['name'].append(x[0])
        #     fetcheddata['org'].append(x[1])
        #     print(fetcheddata['name'])

        # cursor.execute("SELECT * FROM event_record WHERE ename = %s", (bname,))
        # eventdata = cursor.fetchone()
        # print(eventdata[0])
        eventdata = fetchEventRecord.objects.all()
        # id not exist in table then rest all columns data will be fetch
        print(eventdata)
        return render(request,'public/managerServices/showEvent.html',{'event':eventdata,'name':name})
    else:
        return render(request,'login_page.html')
