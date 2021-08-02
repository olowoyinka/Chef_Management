from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def guest_home(request):
    return render(request, "Guest/landing_page.html")

def login(request):
    return render(request, "Guest/login.html")

def register(request):
    return render(request, "Guest/register.html")

def vendor_register(request):
    return render(request, "Guest/vendor_register.html")