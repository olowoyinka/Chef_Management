import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from chef_management_app.EmailBackEnd import EmailBackEnd


def GetLogin(request):
    return render(request,"Home/login.html")


def PostLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse('admin'))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("home"))
            else:
                return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/login")


def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))