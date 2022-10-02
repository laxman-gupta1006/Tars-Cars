from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from contactus.models import Contactus
def aboutus(request):
    return render(request,"aboutus.html",{})
def home(request):
    return render(request,"home.html",{})
def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        try:
            Contactus.objects.create(name=name,email=email,message=message)
            return render(request,"home.html")
        except:
            return render(request,"contactus.html",{"msg":"Unable to send"})
    if request.method == 'GET':
        return render(request,"contactus.html",{"msg":""})
def loginrequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"home.html",{"errormsg":""})
        else:
            return render(request,"home.html",{"errormsg":"Username or Password is not correct!"})
    if request.method == 'GET':
        return render(request,"home.html",{})
def logout_view(request):
    logout(request)
    return redirect('/')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST.get('lastname')
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return render(request,"home.html",{"msg":"User registered successfully"})
        except:
            return render(request,"home.html",{"msg":"Unable to register user"})
    if request.method == 'GET':
        return render(request,"home.html",{"msg":""})

