from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


<<<<<<< HEAD
from chef_management_app.Form.chefform import EditChefForm, ChefPhoneForm, ChefAddressForm, EditChefAddressForm
from chef_management_app.models import CustomUser, ChefUser, ChefImages, ChefPhoneNumer, ChefAddress, Country
=======
from chef_management_app.Form.chefform import EditChefForm, EditChefImageForm
from chef_management_app.models import CustomUser, ChefUser
>>>>>>> parent of d3149f3... worked on upload muiltiple feature image for chef


def HomePage(request):
    return render(request, "Chef/home.html")


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

<<<<<<< HEAD
        if len(request.FILES) != 0:
            if len(chef.image_url) > 0:
                if chef.image_url != "chef/login-img.png":
                    os.remove(chef.image_url.path)
                    chef.image_url = request.FILES['image_url']
                else:
                    chef.image_url = request.FILES['image_url']
        else:
            chef.image_url =  None
=======
        if form.is_valid():
            if request.FILES.get('image_url',False):
                image_url = request.FILES['image_url']
                fs = FileSystemStorage()
                filename = fs.save(image_url.name, image_url)
                image_url_pic = fs.url(filename)
            else:
                image_url_pic =  None
>>>>>>> parent of d3149f3... worked on upload muiltiple feature image for chef

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
<<<<<<< HEAD
            chef = ChefUser.objects.get(admin = request.user.id)
            if chef.image_url != "chef/login-img.png":
                os.remove(chef.image_url.path)
            chef.image_url = "chef/login-img.png"
            chef.save()

            messages.success(request,"Successfully Remove User Image")
            return HttpResponseRedirect(reverse("chef_image"))
        except:
            messages.error(request,"Failed to Remove User Image")
            return HttpResponseRedirect(reverse("chef_image"))


def FeatureImageChef(request):
    if request.method!="POST":
        chef = ChefUser.objects.get(admin = request.user.id)
        chefimage = ChefImages.objects.filter(chefuser_id = chef)
        return render(request,"chef/feature_chef_image.html", { "chefs": chefimage })
    else:
        if request.user.id == None:
            return HttpResponseRedirect(reverse("home"))

        chef = ChefUser.objects.get(admin = request.user.id)

        images = request.FILES.getlist('images')

        for image in images:
            photo = ChefImages.objects.create(
                url = image,
                chefuser_id = chef
            )

        try:
            messages.success(request,"Successfully Upload Multiple")
            return HttpResponseRedirect(reverse("feature_chef_image"))
        except:
            messages.error(request,"Failed to Upload Multiple")
            return HttpResponseRedirect(reverse("feature_chef_image"))


def RemoveFeatureImageChef(request, chef_image_id):
    chef = ChefUser.objects.get(admin = request.user.id)
    chefimage = ChefImages.objects.get(id = chef_image_id, chefuser_id = chef)
    if len(chefimage.url) > 0:
        os.remove(chefimage.url.path)
    chefimage.delete()
    messages.success(request,"Remove Image")
    return HttpResponseRedirect(reverse("feature_chef_image"))


def GetAllPhoneNumber(request):
    chef = ChefUser.objects.get(admin = request.user.id)
    phones = ChefPhoneNumer.objects.filter(chefuser_id = chef)
    return render(request,"chef/get_all_phone_number.html",  { "phones":phones })


def PhoneNumberChef(request):
    if request.method!="POST":
        form = ChefPhoneForm()
        return render(request, "chef/phone_number.html", { "form":form } )
    else:
        form = ChefPhoneForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]

            try:
                chef = ChefUser.objects.get(admin = request.user.id)
                phone = ChefPhoneNumer( number =  phone_number, chefuser_id = chef)
                phone.save()
                messages.success(request,"Successfully Added New Phone Number")
                return HttpResponseRedirect(reverse("chef_phone_number"))
            except:
                messages.error(request,"Failed to Register New Phone Number")
                return HttpResponseRedirect(reverse("chef_phone_number"))
        else:
            form = ChefPhoneForm(request.POST)
            return render(request, "chef/phone_number.html", {"form": form})


def EditPhoneNumberChef(request, phone_number_id):
    if request.method!="POST":
        chef = ChefUser.objects.get(admin = request.user.id)
        phone_number = ChefPhoneNumer.objects.get(id = phone_number_id , chefuser_id = chef)
        form = ChefPhoneForm()
        form.fields['phone_number'].initial = phone_number.number
        return render(request, "chef/edit_phone_number.html", { "form":form })
    else:
        form = ChefPhoneForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]

            try:
                chef = ChefUser.objects.get(admin = request.user.id)
                phone = ChefPhoneNumer.objects.get(id = phone_number_id , chefuser_id = chef)
                phone.number = phone_number
                phone.save()
                messages.success(request,"Successfully Updated Phone Number")
                return HttpResponseRedirect(reverse("chef_phone_number", kwargs = { "phone_number_id":phone_number_id }))
            except:
                messages.error(request,"Failed to Update Phone Number")
                return HttpResponseRedirect(reverse("chef_phone_number",  kwargs = { "phone_number_id":phone_number_id }))
        else:
            form = ChefPhoneForm(request.POST)
            return render(request, "chef/edit_phone_number.html", {"form": form})


def RemovePhoneNumberChef(request, phone_number_id):
    chef = ChefUser.objects.get(admin = request.user.id)
    phone = ChefPhoneNumer.objects.get(id = phone_number_id , chefuser_id = chef)
    phone.delete()
    messages.success(request,"Remove Phone Number")
    return HttpResponseRedirect(reverse("get_chef_phone_number"))


def GetAddress(request):
    chef = ChefUser.objects.get(admin = request.user.id)
    address = ChefAddress.objects.filter(chefuser_id = chef).exists()
    if address:
        address = ChefAddress.objects.get(chefuser_id = chef)
        return render(request,"chef/get_address.html",  { "address":address })
    else:
        return render(request,"chef/get_address.html")


def CreateAddress(request):
    if request.method!="POST":
        form = ChefAddressForm()
        return render(request, "chef/create_address.html", { "form":form } )
    else:
        chef = ChefUser.objects.get(admin = request.user.id)
        chef_address = ChefAddress.objects.filter(chefuser_id = chef).exists()
        if chef_address:
            messages.error(request,"Chef Address Exist")
            return HttpResponseRedirect(reverse("create_address"))
        else:
            form = ChefAddressForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["name"]
                country_id = form.cleaned_data["country"]

                try:
                    country_obj = Country.objects.get(id=country_id)
                    Address = ChefAddress( name =  name, country_id = country_obj, chefuser_id = chef)
                    Address.save()
                    messages.success(request,"Successfully Added Address")
                    return HttpResponseRedirect(reverse("create_address"))
                except:
                    messages.error(request,"Failed to Added Address")
                    return HttpResponseRedirect(reverse("create_address"))
            else:
                form = ChefPhoneForm(request.POST)
                return render(request, "chef/create_address.html", {"form": form})
            


def EditAddress(request, addresss_id):
    if request.method!="POST":
        chef = ChefUser.objects.get(admin = request.user.id)
        chef_address = ChefAddress.objects.get(id = addresss_id, chefuser_id = chef)
        form = EditChefAddressForm()
        form.fields['name'].initial = chef_address.name
        form.fields['country'].initial = chef_address.country_id.id
        return render(request, "chef/edit_address.html", { "form":form })
    else:
        form = EditChefAddressForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            country_id = form.cleaned_data["country"]

            try:
                chef = ChefUser.objects.get(admin = request.user.id)
                chef_address = ChefAddress.objects.get(id = addresss_id, chefuser_id = chef)
                chef_address.name = name
                country_obj = Country.objects.get(id=country_id)
                chef_address.country_id = country_obj
                chef_address.save()
                messages.success(request,"Successfully Updated Address")
                return HttpResponseRedirect(reverse("edit_address", kwargs = { "addresss_id":addresss_id }))
            except:
                messages.error(request,"Failed to Update Phone Number")
                return HttpResponseRedirect(reverse("edit_address",  kwargs = { "addresss_id":addresss_id }))
        else:
            form = ChefPhoneForm(request.POST)
            return render(request, "chef/edit_address.html", {"form": form})


def DeleteAddress(request, addresss_id):
   chef = ChefUser.objects.get(admin = request.user.id)
   chef_address = ChefAddress.objects.get(id = addresss_id, chefuser_id = chef)
   chef_address.delete()
   messages.success(request,"Remove Address")
   return HttpResponseRedirect(reverse("get_address"))
=======
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
>>>>>>> parent of d3149f3... worked on upload muiltiple feature image for chef
