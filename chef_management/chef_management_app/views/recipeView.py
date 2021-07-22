from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import os


from chef_management_app.Form.recipeform import AddRecipeForm, EditRecipeForm
from chef_management_app.models import ChefUser, Country, Recipe



def GetRecipe(request):
    chef = ChefUser.objects.get(admin = request.user.id)
    recipes = Recipe.objects.filter(chefuser_id = chef)
    return render(request,"recipe/get_recipe.html",  { "recipes":recipes })


def CreateRecipe(request):
    if request.method!="POST":
        form = AddRecipeForm()
        return render(request, "recipe/create_recipe.html", { "form":form } )
    else:
        form = AddRecipeForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data["name"]
            description=form.cleaned_data["description"]
            method=form.cleaned_data["method"]
            ingredient=form.cleaned_data["ingredient"]
            price=form.cleaned_data["price"]

            if len(request.FILES) != 0:
                image_url = request.FILES['image_url']
            else:
                image_url =  None

            try:
                chef = ChefUser.objects.get(admin = request.user.id)
                photo = Recipe.objects.create(
                    name=name,
                    decription=description,
                    method=method,
                    ingredient=ingredient,
                    price=price,
                    chefuser_id = chef,
                    image_url = image_url
                )
                messages.success(request,"Successfully Added New Recipe")
                return HttpResponseRedirect(reverse("create_recipe"))
            except:
                messages.error(request,"Failed to Added New Recipe")
                return HttpResponseRedirect(reverse("create_recipe"))
        else:
            form = AddRecipeForm()(request.POST)
            return render(request, "recipe/create_recipe.html", {"form": form})


def EditRecipe(request, recipe_id):
    if request.method!="POST":
        chef = ChefUser.objects.get(admin = request.user.id)
        recipe = Recipe.objects.get(id = recipe_id , chefuser_id = chef)
        form = EditRecipeForm()
        form.fields['name'].initial = recipe.name
        form.fields['description'].initial = recipe.decription
        form.fields['method'].initial = recipe.method
        form.fields['ingredient'].initial = recipe.ingredient
        form.fields['price'].initial = recipe.price
        return render(request, "recipe/edit_recipe.html", { "form":form } )
    else:
        form = EditRecipeForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data["name"]
            description=form.cleaned_data["description"]
            method=form.cleaned_data["method"]
            ingredient=form.cleaned_data["ingredient"]
            price=form.cleaned_data["price"]

            try:
                chef = ChefUser.objects.get(admin = request.user.id)
                recipe = Recipe.objects.get(id = recipe_id , chefuser_id = chef)
                recipe.name = name
                recipe.decription = description
                recipe.method = method
                recipe.ingredient = ingredient
                recipe.price = price

                if len(request.FILES) != 0:
                    os.remove(recipe.image_url.path)                
                    image_url = request.FILES['image_url']
                    recipe.image_url = image_url
                
                recipe.save()

                messages.success(request,"Successfully Edited Recipe")
                return HttpResponseRedirect(reverse("edit_recipe", kwargs = { "recipe_id":recipe_id }))
            except:
                messages.error(request,"Failed to Edit Recipe")
                return HttpResponseRedirect(reverse("edit_recipe", kwargs = { "recipe_id":recipe_id }))
        else:
            form = AddRecipeForm()(request.POST)
            return render(request, "recipe/edit_recipe.html", {"form": form})


def DeleteRecipe(request, recipe_id):
    chef = ChefUser.objects.get(admin = request.user.id)
    recipe = Recipe.objects.get(id = recipe_id , chefuser_id = chef)
    if len(recipe.image_url) > 0:
        os.remove(recipe.image_url.path)
    recipe.delete()
    messages.success(request,"Remove Recipe")
    return HttpResponseRedirect(reverse("get_recipe"))