from django.shortcuts import render

# Create your views here.
def resetpass(request):
    return render(request,'resetPassword.html')