from django.shortcuts import render
import mysql.connector as mysql
dpassword=''
demail=''
# Create your views here.
def loginaction(request):
    global dpassword,demail,dprofile
    if request.method == 'POST':
        d = request.POST
        for key, value in d.items():
            if key == 'lemail':
                demail = value
            if key == 'lpassword':
                dpassword = value
            if key == 'lradio1':
                dprofile = value
        db = mysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="ssbm_db"
        )
        cursor = db.cursor()
        cursor.execute('SELECT * FROM signup_db')
        data = cursor.fetchall()
        print(dprofile)
        for row in data:
            print(data)
            if row[2] == demail and row[3] == dpassword and row[5] == dprofile:
                request.session['name'] = row[1]
                request.session['email'] = row[2]
                request.session['customer_fields'] = row[5]
                con = {'name': row[1], 'email': row[2], 'customer_fields': row[5]}
                return render(request, 'prompt_message2.html', {'con': con})
                # users = {'name': row[0], 'email': row[1], 'customer_fields': row[4]}
                # return render(request, 'public/userMainPage.html',{'users':users})
        return render(request, 'login_page.html', {'error': 'useremail or password may be worng!!!','error1':'please re-check profile'})
    else:
        return render(request, 'login_page.html',{'message':'please fill the form'})