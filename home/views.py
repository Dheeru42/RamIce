from django.shortcuts import render,redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login

def index(request):
    if request.user.is_anonymous:
        return render(request,'login.html')
    return render(request,'index.html')

def loginuser(request):
    if request.method=='POST':
        uname = request.POST.get('user')
        passw = request.POST.get('pass')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('/login')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('ema')
        phone = request.POST.get('num')
        cont = Contact(name=name,email=email,phone=phone,date=datetime.today())
        cont.save()
        messages.success(request, "Your Message is Sent")
    return render(request,'cont.html')

def about(request):
    return render(request,'about.html')