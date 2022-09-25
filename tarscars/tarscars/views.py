from django.shortcuts import render
from django.http import HttpResponse

def aboutus(request):
    return render(request,"aboutus.html",{})
def home(request):
    return render(request,"home.html",{})
def contactus(request):
    return render(request,"contactus.html",{})

