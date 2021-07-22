"""chef_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
#from chef_management_app import views
from chef_management_app.views import homeView
from chef_management_app.views import adminView
from chef_management_app.views import chefView
from chef_management_app.views import recipeView
from chef_management_app.views import regularUserView
from chef_management import settings


urlpatterns = [
    path('', homeView.HomePage, name="home"),
    path('admin/', admin.site.urls),

    #Login
    path('login', homeView.Login, name="login"),
    path('logout', homeView.LogOut, name="logout"),

    #Admin
    path('admin', adminView.HomePage, name="admin_home"),
 
    #Chef
    path('chef_home', chefView.HomePage, name="chef_home"),
    path('chef_register', homeView.ChefRegister, name="chef_register"),
    path('edit_chef', chefView.EditChef, name="edit_chef"),
    path('chef_image', chefView.ImageChef, name="chef_image"),
    path('remove_chef_image', chefView.RemoveImageChef, name="remove_chef_image"),
    path('feature_chef_image', chefView.FeatureImageChef, name="feature_chef_image"),
    path('remove_feature_chef_image/<str:chef_image_id>', chefView.RemoveFeatureImageChef, name="remove_feature_chef_image"),

    #User
    path('user_home', regularUserView.HomePage, name="user_home"),
    path('user_register', homeView.RegularUserRegister, name="user_register"),
    path('edit_user', regularUserView.EditRegularUser, name="edit_user"),
    path('user_image', regularUserView.ImageRegularUser, name="user_image"),
    path('remove_user_image', regularUserView.RemoveImageRegularUser, name="remove_user_image"),


    #Recipe
    path('create_recipe', recipeView.CreateRecipe, name="create_recipe"),
    path('get_recipe', recipeView.GetRecipe, name="get_recipe"),
    path('edit_recipe/<str:recipe_id>', recipeView.EditRecipe, name="edit_recipe"),
    path('delete_recipe/<str:recipe_id>', recipeView.DeleteRecipe, name="delete_recipe")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)