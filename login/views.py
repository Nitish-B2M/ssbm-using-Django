from django.shortcuts import render
from signup.models import userData


dpassword=''
demail=''
dprofile=''
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
        try:
            Table_email = userData.objects.get(email=demail,password=dpassword,customer_fields=dprofile)
            if Table_email:
                request.session['name']=Table_email.name
                request.session['email']=Table_email.email
                request.session['profile']=Table_email.customer_fields
                return render(request, 'prompt_message2.html', {'name':Table_email.name,'profile':Table_email.customer_fields})
            else:
                return render(request, 'login_page.html', {'error': 'useremail or password may be worng!!!','error1':'please re-check profile,'})
        except Exception as e:
            print(e)
            return render(request, 'login_page.html', {'error': 'useremail or password may be worng!!!','error1':'please re-check profile,'})
    else:
        return render(request, 'login_page.html',{'message':'please fill the form'})