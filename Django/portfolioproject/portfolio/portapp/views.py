from django.shortcuts import render
from django.http import request
from portapp.models import CustomUser

# Create your views here.
def index(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        signemail = request.POST.get('signemail')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        passwordcon = request.POST.get('passwordcon')
        
        print("Full Name : ", fullname)
        print("Signemail : ", signemail)
        print("Phone Number : ", phone)
        print("Password : ", password)
        print("Re - Password : ", passwordcon)
        

    return render(request, "home/index.html")
