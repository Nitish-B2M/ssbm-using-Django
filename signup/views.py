from django.shortcuts import render
from .models import userData
from .utils import send_email

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
        elif dpassword.isalnum():
            return render(request, 'signup_page.html', {'error18': 'Password must contain some special characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif dpassword.isalpha():
            return render(request, 'signup_page.html', {'error20': 'Password must contain some lower case or upper case characters','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        elif dpassword.isspace():
            return render(request, 'signup_page.html', {'error21': 'Password must not contain any space','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
        else:
            signupTable = userData.objects.filter(email=demail)
            if signupTable:
                return render(request, 'signup_page.html', {'error22': 'Email already exists','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio':dpassword, 'dskey': dskey})
            else: 
                if not mail_formatter_to_new_client(dname,demail):
                    return render(request, 'signup_page.html', {'error24': 'Email not sent','dname': dname, 'demail': demail, 'dpassword': dpassword, 'drepassword': drepassword, 'dradio': dradio, 'dskey': dskey})
                signupTable = userData(name=dname, email=demail, password=dpassword, repassword=drepassword, customer_fields=dradio, skey=dskey)
                signupTable.save()
                return render(request, 'prompt_message.html', {'message': 'User created successfully'})
    else:
        return render(request, 'signup_page.html', {'message': 'Please fill the form'})


def mail_formatter_to_new_client(dname,demail):
    msg = 'Hello '+dname+' you have successfully login to our website, we are happy to see you here. Click on the link below to login to our website. http://127.0.0.1:8000/login/'
    subject = 'Login Successfull from SSBM'
    from_email = 'dump.yard.area@gmail.com'
    if send_email(subject,msg,from_email,[demail]):
        return True
    else:
        return False
