from django.shortcuts import render,redirect

# Create your views here.
# logout and session deletion
def logoutaction(request):
    if request.session.has_key('name'):
        del request.session['name']
        del request.session['email']
        del request.session['profile']

        # return render(request,'login_page.html')
        return redirect('/login/')
    else:
        return render(request,'login_page.html')