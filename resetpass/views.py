from django.shortcuts import render
from signup.models import userData

# Create your views here.

# from email.message import EmailMessage
# import ssl
# import smtplib

def resetpass(request):
    if request.method == 'POST':
        email = request.POST['email']
        skey = request.POST['skey']
        option = request.POST['sradio1']
        password = request.POST['password']
        cond = userData.objects.filter(email=email, skey=skey, customer_fields=option)
        prevPassword = userData.objects.filter(email=email, skey=skey, customer_fields=option).values('password')
        if cond:
            if prevPassword == password:
                return render(request, 'resetPassword.html', {'error': 'Password Matched with Previous Password', 'email': email, 'skey': skey, 'option': option})
            elif len(password) < 8:
                return render(request, 'resetPassword.html', {'error': 'Password must be at least 8 characters long', 'email': email, 'skey': skey, 'option': option})
            elif password.isalpha():
                return render(request, 'resetPassword.html', {'error': 'Password must contain at least one number', 'email': email, 'skey': skey, 'option': option})
            elif password.isnumeric():
                return render(request, 'resetPassword.html', {'error': 'Password must contain at least one character', 'email': email, 'skey': skey, 'option': option})
            else:
                userData.objects.filter(email=email, skey=skey, customer_fields=option).update(password = password)
                return render(request, 'resetPassword.html', {'message': 'Password Reset Successfully'})
        else:
            print("Invalid Credentials")
            return render(request, 'resetPassword.html', {'error': 'Invalid Credentials'})
    return render(request,'resetPassword.html')