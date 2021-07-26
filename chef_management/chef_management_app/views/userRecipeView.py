from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import os
from django.core.paginator import Paginator

from chef_management_app.models import ChefUser, Country, Recipe, RecipeImages



def GetRecipe(request):
    p = Paginator(Recipe.objects.all().order_by('-id'), 2)
    page = request.GET.get('page')
    recipes = p.get_page(page)
    nums = "a" * recipes.paginator.num_pages
    return render(request,"userrecipe/get_recipe.html",  { "recipes":recipes, 'nums':nums })


def GetRecipeById(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    recipeImages = RecipeImages.objects.filter(recipe_id = recipe_id)
    return render(request, "userrecipe/get_recipe_id.html", { "recipe":recipe, "recipeImages":recipeImages } )