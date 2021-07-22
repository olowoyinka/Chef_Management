import datetime
import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


#file path
def filepath_chef(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('chef/', filename)

def filepath_chef_image(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('chef_images/', filename)

def filepath_user(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('user/', filename)

def filepath_recipe(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('recipe/', filename)

def filepath_recipe_image(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('recipe_images/', filename)


# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Chef"),(3,"Regular"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)


class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class ChefUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    chef_name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to=filepath_chef,null=True,blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class RegularUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=filepath_user,null=True,blank=True)
    phone_number = models.CharField(max_length=255)
    join_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    decription = models.TextField()
    method = models.TextField()
    ingredient = models.TextField()
    image_url = models.ImageField(upload_to=filepath_recipe,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    chefuser_id = models.ForeignKey(ChefUser, on_delete=models.CASCADE)
    objects = models.Manager()


class Continent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    objects = models.Manager()


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    continent_id = models.ForeignKey(Continent, on_delete=models.CASCADE)
    objects = models.Manager()


class ChefAddress(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    chefuser_id = models.ForeignKey(ChefUser, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    objects = models.Manager()


class ChefImages(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.ImageField(upload_to=filepath_chef_image,null=True,blank=False)
    chefuser_id = models.ForeignKey(ChefUser, on_delete=models.CASCADE)
    objects = models.Manager()


class ChefPhoneNumer(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255)
    chefuser_id = models.ForeignKey(ChefUser, on_delete=models.CASCADE)
    objects = models.Manager()


class RecipeAddress(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    objects = models.Manager()


class RecipeCommentary(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    show_comment = models.BooleanField(default=True)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    regularuser_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    objects = models.Manager()


class RecipeImages(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.ImageField(upload_to=filepath_recipe_image,null=True,blank=False)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    objects = models.Manager()


class RecipeRating(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    regularuser_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    objects = models.Manager()


class RecipeSurvey(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    question_one = models.TextField()
    question_two = models.TextField()
    question_three = models.TextField()
    question_four = models.TextField()
    question_five = models.TextField()
    question_six = models.TextField()
    question_seven = models.TextField()
    question_eight = models.TextField()
    question_nine = models.TextField()
    question_ten = models.TextField()
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    regularuser_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    objects = models.Manager()


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    chefuser_id = models.ForeignKey(ChefUser, on_delete=models.CASCADE)
    regularuser_id = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    objects = models.Manager()


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            ChefUser.objects.create(admin=instance)
        if instance.user_type==3:
            RegularUser.objects.create(admin=instance)


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.chefuser.save()
    if instance.user_type==3:
        instance.regularuser.save()