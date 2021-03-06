from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from chef_management_app.EmailBackEnd import EmailBackEnd
from chef_management_app.Form.chefform import AddChefForm
from chef_management_app.Form.regularuserform import AddRegularUserForm
from chef_management_app.models import CustomUser

# Create your views here.
def HomePage(request):
    return render(request, "Home/welcome.html")


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
                return HttpResponseRedirect(reverse('admin_home'))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("chef_home"))
            else:
                return HttpResponseRedirect(reverse("user_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect(reverse("login"))


def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def GetChefRegister(request):
    form = AddChefForm()
    return render(request, "chef/register.html", { "form":form } )


def PostChefRegister(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddChefForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            chef_name=form.cleaned_data["chef_name"]


            try:
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
                user.chefuser.chef_name = chef_name
                user.save()
                messages.success(request,"Successfully Added New Chef")
                return HttpResponseRedirect(reverse("chef_register"))
            except:
                messages.error(request,"Failed to Register Staff")
                return HttpResponseRedirect(reverse("chef_register"))
        else:
            form = AddChefForm(request.POST)
            return render(request, "chef/register.html", {"form": form})


def GetRegularUserRegister(request):
    form = AddRegularUserForm()
    return render(request, "regularuser/register.html", { "form":form } )


def PostRegularUserRegister(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddRegularUserForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            phone_number=form.cleaned_data["phone_number"]

            try:
                user = CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.regularuser.phone_number = phone_number
                user.save()
                messages.success(request,"Successfully Added New User")
                return HttpResponseRedirect(reverse("user_register"))
            except:
                messages.error(request,"Failed to Register New User")
                return HttpResponseRedirect(reverse("user_register"))
        else:
            form = AddRegularUserForm(request.POST)
            return render(request, "regularuser/register.html", {"form": form})