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
    return render(request, "Guest/vendor_register.html")

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