from django.shortcuts import render
import mysql.connector as mysql
dname = ''
demail = ''
dpassword = ''
drepassword = ''
dradio = ''
dskey = ''
# Create your views here.
def signupaction(request):
    global dname, demail, dpassword, drepassword
    if request.method == 'POST':
        d = request.POST
        for key, value in d.items():
            if key == 'sname':
                dname = value
            elif key == 'semail':
                demail = value
            elif key == 'spassword':
                dpassword = value
            elif key == 'srepassword':
                drepassword = value
            elif key == 'sradio':
                dradio = value
            elif key == 'skey':
                dskey = value
        if dname == ' ' or demail == ' ' or dpassword == ' ' or drepassword == ' ' or dradio == ' ' or dskey == ' ':
            return render(request, 'signup_page.html', {'error1': 'Please fill the fields with valid data','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword , 'dskey': dskey})
        elif dpassword != drepassword:
            return render(request, 'signup_page.html', {'error2': 'Password and Re-Password does not match','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif len(dpassword) < 8:
            return render(request, 'signup_page.html', {'error3': 'Password must be of 8 characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif len(dpassword) > 16:
            return render(request, 'signup_page.html', {'error4': 'Password must be of 16 characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif len(dname) > 20:
            return render(request, 'signup_page.html', {'error5': 'Name must be of 20 characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif len(demail) > 30:
            return render(request, 'signup_page.html', {'error6': 'Email must be of 30 characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif len(dname) < 3:
            return render(request, 'signup_page.html', {'error7': 'Name must be of 3 characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif len(demail) < 10:
            return render(request, 'signup_page.html', {'error8': 'Email must be of 10 characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif demail.find('@') == -1 or demail.find('.') == -1:
            return render(request, 'signup_page.html', {'error9': 'Email must be valid','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif demail.find('@') > demail.find('.'):
            return render(request, 'signup_page.html', {'error10': 'Email must be valid','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif demail.find('@') == 0 or demail.find('.') == 0:
            return render(request, 'signup_page.html', {'error11': 'Email must be valid','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif demail.find('@') == len(demail) - 1 or demail.find('.') == len(demail) - 1:
            return render(request, 'signup_page.html', {'error12': 'Email must be valid','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif demail.find('@') == demail.find('.') - 1:
            return render(request, 'signup_page.html', {'error13': 'Email must be valid','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif demail.find('@') == demail.find('.') + 1:
            return render(request, 'signup_page.html', {'error14': 'Email must be valid','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif len(dskey) < 4 or len(dskey) > 8:
            return render(request, 'signup_page.html', {'error23': 'Key must be length of 4 to 8','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        # elif dname.startswith(dname.index(0).isnumeric()):
        #     return render(request, 'signup_page.html', {'error15': 'Name must be start with alphabet','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        # elif dpassword.startswith(dpassword.index(0).isnumeric()):
        #     return render(request, 'signup_page.html', {'error16': 'Password must be start with alphabet','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword})
        # elif demail.startswith(demail.index(0).isnumeric()):
        #     return render(request, 'signup_page.html', {'error17': 'Email must be start with alphabet','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword})
        # password must contain some basic format
        elif dpassword.isalnum():
            return render(request, 'signup_page.html', {'error18': 'Password must contain some special characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        # elif dpassword.islower():
        #     return render(request, 'signup_page.html', {'error19': 'Password must contain some upper case characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword})
        elif dpassword.isalpha():
            return render(request, 'signup_page.html', {'error20': 'Password must contain some lower case or upper case characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif dpassword.isspace():
            return render(request, 'signup_page.html', {'error21': 'Password must not contain any space','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        else:
            db = mysql.connect(
                host = 'localhost',
                user = 'root',
                passwd = 'root',
                database = 'ssbm_db'
            )
            cursor = db.cursor()
            cursor.execute('SELECT * FROM signup_db WHERE email = %s', (demail,))
            data = cursor.fetchall()
            if len(data) > 0:
                return render(request, 'signup_page.html', {'error22': 'Email already exists','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
            else:
                db = mysql.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "root",
                    database = "ssbm_db"
                )
                cursor = db.cursor()
                cursor.execute("INSERT INTO signup_db(name, email, password, repassword, customer_fields, skey) VALUES(%s, %s, %s, %s, %s, %s)", (dname, demail, dpassword, drepassword, dradio, dskey))
                db.commit()
                return render(request, 'prompt_message.html', {'message': 'User created successfully'})
    else:
        return render(request, 'signup_page.html', {'message': 'Please fill the form'})



    #     dname = request.POST.get('name')
    #     demail = request.POST.get('email')
    #     dpassword = request.POST.get('password')
    #     drepassword = request.POST.get('repassword')
    #     if dpassword == drepassword:
    #         db = mysql.connect(
    #             host = "localhost",
    #             user = "root",
    #             passwd = "root",
    #             database = "ssbm_db"
    #         )
    #         cursor = db.cursor()
    #         cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (dname, demail, dpassword))
    #         db.commit()
    #         return render(request, 'signup.html', {'message': 'User created successfully!'})
    #     else:
    #         return render(request, 'signup.html', {'message': 'Password does not match!'})
    # return render(request, 'signup/signup.html')