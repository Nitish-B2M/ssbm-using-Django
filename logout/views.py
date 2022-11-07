from django.shortcuts import render

# Create your views here.
# logout and session deletion
def logoutaction(request):
    if request.session.has_key('name'):
        del request.session['name']
        del request.session['email']
        return render(request,'login_page.html')
    else:
        return render(request,'login_page.html')

        