from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from chef_management_app.Form.regularuserform import EditRegularUserForm, EditRegularUserImageForm
from chef_management_app.models import CustomUser, RegularUser



def HomePage(request):
    return render(request, "RegularUser/home.html")


def GetEditRegularUser(request):
    regularuser = RegularUser.objects.get(admin = request.user.id)
    form = EditRegularUserForm()
    form.fields['first_name'].initial = regularuser.admin.first_name
    form.fields['last_name'].initial = regularuser.admin.last_name
    form.fields['phone_number'].initial = regularuser.phone_number
    return render(request,"regularuser/edit_user.html", {"form":form, "username":regularuser.admin.username, "email":regularuser.admin.email })


def PostEditRegularUser(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.user.id == None:
            return HttpResponseRedirect(reverse("home"))

        form = EditRegularUserForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]

            try:
                user = CustomUser.objects.get(id = request.user.id)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                regularuser = RegularUser.objects.get(admin = request.user.id)
                regularuser.phone_number = phone_number
                regularuser.save()

                messages.success(request,"Successfully Edited User")
                return HttpResponseRedirect(reverse("edit_user"))
            except:
                messages.error(request,"Failed to Edit User")
                return HttpResponseRedirect(reverse("edit_user"))
        else:
            form = EditRegularUserForm(request.POST)
            regularuser = RegularUser.objects.get(admin = request.user.id)
            return render(request,"regularuser/edit_user.html", {"form":form, "username":regularuser.admin.username, "email":regularuser.admin.email})


def GetImageRegularUser(request):
    regularuser = RegularUser.objects.get(admin = request.user.id)
    form = EditRegularUserImageForm()
    return render(request,"regularuser/edit_user_image.html", {"form":form, "email":regularuser.admin.email, "image_url":regularuser.image_url })


def PostImageRegularUser(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.user.id == None:
            return HttpResponseRedirect(reverse("home"))

        form = EditRegularUserImageForm(request.POST, request.FILES)

        if form.is_valid():
            if request.FILES.get('image_url',False):
                image_url = request.FILES['image_url']
                fs = FileSystemStorage()
                filename = fs.save(image_url.name, image_url)
                image_url_pic = fs.url(filename)
            else:
                image_url_pic =  None

            try:
                regularuseruser = RegularUser.objects.get(admin = request.user.id)

                if image_url_pic != None:
                    regularuseruser.image_url = image_url_pic
                regularuseruser.save()

                messages.success(request,"Successfully Edited User")
                return HttpResponseRedirect(reverse("edit_user_image"))
            except:
                messages.error(request,"Failed to Edit User")
                return HttpResponseRedirect(reverse("edit_user_image"))
        else:
            form = EditRegularUserForm(request.POST)
            regularuser = RegularUser.objects.get(admin = request.user.id)
            return render(request,"regularuser/edit_user_image.html", {"form":form, "email":regularuser.admin.email, "image_url":regularuser.image_url})


def RemoveImageRegularUser(request):
        if request.user.id == None:
            return HttpResponseRedirect(reverse("home"))            

        try:
            fs = FileSystemStorage()
            regularuser = RegularUser.objects.get(admin = request.user.id)
            fs.delete(regularuser.image_url)
            
            regularuser.image_url = ""
            regularuser.save()

            messages.success(request,"Successfully Remove User Image")
            return HttpResponseRedirect(reverse("edit_user_image"))
        except:
            messages.error(request,"Failed to Remove User Image")
            return HttpResponseRedirect(reverse("edit_user_image"))