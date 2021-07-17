from django.db import models

# Create your models here.
class ChefUser(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    chef_name = models.CharField(max_length=255)
    image_url = models.FileField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    join_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class RegularUser(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_url = models.FileField()
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField(max_length=20)
    password = models.CharField(max_length=255)
    join_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    decription = models.TextField()
    method = models.TextField()
    ingredient = models.TextField()
    image_url = models.FileField()
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
    continent_id = models.ForeignKey(Continent, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    objects = models.Manager()


class ChefImages(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.FileField()
    chefuser_id = models.ForeignKey(ChefUser, on_delete=models.CASCADE)
    objects = models.Manager()


class ChefPhoneNumer(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    chefuser_id = models.ForeignKey(ChefUser, on_delete=models.CASCADE)
    objects = models.Manager()


class RecipeAddress(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    continent_id = models.ForeignKey(Continent, on_delete=models.CASCADE)
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
    url = models.FileField()
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