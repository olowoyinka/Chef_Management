from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


#from student_management_app.forms import AddStudentForm, EditStudentForm
from chef_management_app.models import CustomUser


def GetRegister(request):
    return render(request,"chef/register.html")

def PostRegister(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        chef_name = request.POST.get("chef_name")
        #image_url = models.FileField()
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.chefuser.chef_name =  chef_name
            user.save()
            messages.success(request,"Successfully Added New Chef")
            return HttpResponseRedirect(reverse("chef_register"))
        except:
            messages.error(request,"Failed to Register Staff")
            return HttpResponseRedirect(reverse("chef_register"))