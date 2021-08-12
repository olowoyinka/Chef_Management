from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Guest
def guest_home(request):
    return render(request, "Guest/landing_page.html")

def login(request):
    return render(request, "Guest/login.html")

def register(request):
    return render(request, "Guest/register.html")

def vendor_register(request):
    return render(request, "Guest/chef.html")

#Chef
def chef_home(request):
    return render(request, "Chef/chef_home.html")

def new_recipe(request):
    return render(request, "Chef/new_recipe.html")

def recipe(request):
    return render(request, "Chef/recipe.html")

def update_delete(request):
    return render(request, "Chef/edit_recipe.html")

def customer_feedback(request):
    return render(request, "Chef/customer_feedback.html")

#Regular
def regular_home(request):
    return render(request, "Regular/home.html")

def recipe(request):
    return render(request, "Regular/recipe.html")

def chef(request):
    return render(request, "Regular/chef.html")

def ingredient(request):
    return render(request, "Regular/ingredient.html")

def method(request):
    return render(request, "Regular/method.html")

def quiz_home(request):
    return render(request, "Regular/quiz.html")

def review(request):
    return render(request, "Regular/review.html")

def favourite(request):
    return render(request, "Regular/favourite.html")

def result(request):
    return render(request, "Regular/result.html")