from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from chef_management_app.Form.chefform import AddChefForm, EditChefForm, EditChefImageForm
from chef_management_app.models import CustomUser, ChefUser


def GetRegister(request):
    form = AddChefForm()
    return render(request, "chef/register.html", { "form":form } )


def PostRegister(request):
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


def GetEditChef(request):
    chefuser = ChefUser.objects.get(admin = request.user.id)
    form = EditChefForm()
    form.fields['first_name'].initial = chefuser.admin.first_name
    form.fields['last_name'].initial = chefuser.admin.last_name
    form.fields['chef_name'].initial = chefuser.chef_name
    return render(request,"chef/edit_chef.html", {"form":form, "username":chefuser.admin.username, "email":chefuser.admin.email })


def PostEditChef(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.user.id == None:
            return HttpResponseRedirect(reverse("home"))

        form = EditChefForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            chef_name = form.cleaned_data["chef_name"]

            try:
                user = CustomUser.objects.get(id = request.user.id)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                chefuser = ChefUser.objects.get(admin = request.user.id)
                chefuser.chef_name = chef_name
                chefuser.save()

                messages.success(request,"Successfully Edited Chef")
                return HttpResponseRedirect(reverse("edit_chef"))
            except:
                messages.error(request,"Failed to Edit Chef")
                return HttpResponseRedirect(reverse("edit_chef"))
        else:
            form = EditChefForm(request.POST)
            chefuser = ChefUser.objects.get(admin = request.user.id)
            return render(request,"chef/edit_chef.html", {"form":form, "username":chefuser.admin.username, "email":chefuser.admin.email})


def GetImageChef(request):
    chefuser = ChefUser.objects.get(admin = request.user.id)
    form = EditChefImageForm()
    return render(request,"chef/edit_chef_image.html", {"form":form, "email":chefuser.admin.email, "image_url":chefuser.image_url })


def PostImageChef(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.user.id == None:
            return HttpResponseRedirect(reverse("home"))

        form = EditChefImageForm(request.POST, request.FILES)

        if form.is_valid():
            if request.FILES.get('image_url',False):
                image_url = request.FILES['image_url']
                fs = FileSystemStorage()
                filename = fs.save(image_url.name, image_url)
                image_url_pic = fs.url(filename)
            else:
                image_url_pic =  None

            try:
                chefuser = ChefUser.objects.get(admin = request.user.id)

                if image_url_pic != None:
                    chefuser.image_url = image_url_pic
                chefuser.save()

                messages.success(request,"Successfully Edited Chef")
                return HttpResponseRedirect(reverse("edit_chef_image"))
            except:
                messages.error(request,"Failed to Edit Chef")
                return HttpResponseRedirect(reverse("edit_chef_image"))
        else:
            form = EditChefForm(request.POST)
            chefuser = ChefUser.objects.get(admin = request.user.id)
            return render(request,"chef/edit_chef_image.html", {"form":form, "email":chefuser.admin.email, "image_url":chefuser.image_url})


def RemoveImageChef(request):
        if request.user.id == None:
            return HttpResponseRedirect(reverse("home"))            

        try:
            fs = FileSystemStorage()
            chefuser = ChefUser.objects.get(admin = request.user.id)
            fs.delete(chefuser.image_url)
            
            chefuser.image_url = ""
            chefuser.save()

            messages.success(request,"Successfully Remove Chef")
            return HttpResponseRedirect(reverse("edit_chef_image"))
        except:
            messages.error(request,"Failed to Remove Chef")
            return HttpResponseRedirect(reverse("edit_chef_image"))