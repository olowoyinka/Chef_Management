from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import os


from chef_management_app.Form.recipeform import AddRecipeForm
from chef_management_app.models import ChefUser, Country, Recipe



def CreateRecipe(request):
    if request.method!="POST":
        form = AddRecipeForm()
        return render(request, "recipe/create_recipe.html", { "form":form } )
    else:
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            description=form.cleaned_data["description"]
            method=form.cleaned_data["method"]
            ingredient=form.cleaned_data["ingredient"]
            price=form.cleaned_data["price"]

            try:
                chef = ChefUser.objects.get(admin = request.user.id)
                photo = Recipe.objects.create(
                    name=name,
                    description=description,
                    method=method,
                    ingredient=ingredient,
                    price=price
                )
                messages.success(request,"Successfully Added New Recipe")
                return HttpResponseRedirect(reverse("create_recipe"))
            except:
                messages.error(request,"Failed to Added New Recipe")
                return HttpResponseRedirect(reverse("create_recipe"))
        else:
            form = AddRecipeForm()(request.POST)
            return render(request, "recipe/create_recipe.html", {"form": form})