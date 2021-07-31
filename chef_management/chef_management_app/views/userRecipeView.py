from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import os
from django.core.paginator import Paginator

from chef_management_app.models import RecipeCommentary, Recipe, RecipeImages, RegularUser, RecipeRating



def GetRecipe(request):
    p = Paginator(Recipe.objects.all().order_by('-id'), 2)
    page = request.GET.get('page')
    recipes = p.get_page(page)
    nums = "a" * recipes.paginator.num_pages
    return render(request,"userrecipe/get_recipe.html",  { "recipes":recipes, 'nums':nums })


def GetRecipeById(request, recipe_id):
    if request.method == 'POST':
        message = request.POST['message']
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
    else:
        recipe = Recipe.objects.get(id = recipe_id)
        user_obj = RegularUser.objects.get(admin = request.user.id)
        recipeImages = RecipeImages.objects.filter(recipe_id = recipe_id)
        recipeCommentary = RecipeCommentary.objects.filter(recipe_id = recipe_id)
        rating = RecipeRating.objects.get(recipe_id = recipe, regularuser_id = user_obj).rating
        return render(request, "userrecipe/get_recipe_id.html", { "recipe" : recipe, "recipeImages" : recipeImages, "user" : user_obj.image_url, "commentary" : recipeCommentary, "rating" : rating } )


def GeteRecipeById(request, recipe_id):
    if request.method == 'POST':
        rating = request.POST['rating']
        user_obj = RegularUser.objects.get(admin = request.user.id)
        recipe_obj = Recipe.objects.get(id = recipe_id)
        recipeRating_obj = RecipeRating.objects.filter(recipe_id = recipe_obj, regularuser_id = user_obj).exists()

        if(recipeRating_obj):
            recipeRating_obj = RecipeRating.objects.get(recipe_id = recipe_obj, regularuser_id = user_obj)
            recipeRating_obj.rating = rating
            recipeRating_obj.save()
        
        else:
            new_Rating = RecipeRating(
                rating = rating,
                regularuser_id = user_obj,
                recipe_id = recipe_obj
            )

            new_Rating.save()

        return JsonResponse({'success':'true', 'score': rating}, safe=False)