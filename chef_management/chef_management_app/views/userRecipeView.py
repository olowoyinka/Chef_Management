from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import os
from django.core.paginator import Paginator

from chef_management_app.models import RecipeCommentary, Recipe, RecipeImages, RegularUser



def GetRecipe(request):
    p = Paginator(Recipe.objects.all().order_by('-id'), 2)
    page = request.GET.get('page')
    recipes = p.get_page(page)
    nums = "a" * recipes.paginator.num_pages
    return render(request,"userrecipe/get_recipe.html",  { "recipes":recipes, 'nums':nums })


def GetRecipeById(request, recipe_id):
    if request.method != 'POST':
        recipe = Recipe.objects.get(id = recipe_id)
        user_obj = RegularUser.objects.get(admin = request.user.id).image_url
        recipeImages = RecipeImages.objects.filter(recipe_id = recipe_id)
        recipeCommentary = RecipeCommentary.objects.filter(recipe_id = recipe_id)
        return render(request, "userrecipe/get_recipe_id.html", { "recipe":recipe, "recipeImages":recipeImages, "user" : user_obj, "commentary" : recipeCommentary } )
    else:
        message = request.POST['message']
        recipe_id = request.POST['recipe_id']
        user_obj = RegularUser.objects.get(admin = request.user.id)
        recipe_obj = Recipe.objects.get(id = recipe_id)

        new_commentary = RecipeCommentary(
            message = message,
            regularuser_id = user_obj,
            recipe_id = recipe_obj,
            show_comment = True
        )

        new_commentary.save()

        response = {
            "message" : message,
            "created" : "Now",
        }

        return JsonResponse(response)

        