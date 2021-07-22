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
    path('login', homeView.GetLogin, name="login"),
    path('postlogin', homeView.PostLogin, name="postlogin"),
    path('logout', homeView.LogOut, name="logout"),

    #Admin
    path('admin', adminView.HomePage, name="admin_home"),
 
    #Chef
<<<<<<< HEAD
    path('chef', chefView.HomePage, name="chef_home"),
    path('chef_register', homeView.ChefRegister, name="chef_register"),
    path('chef_edit', chefView.EditChef, name="edit_chef"),
    path('chef_image', chefView.ImageChef, name="chef_image"),
    path('chef_image_remove', chefView.RemoveImageChef, name="remove_chef_image"),
    path('chef_feature_image', chefView.FeatureImageChef, name="feature_chef_image"),
    path('chef_feature_image/<str:chef_image_id>', chefView.RemoveFeatureImageChef, name="remove_feature_chef_image"),
    path('chef_phone_number', chefView.GetAllPhoneNumber, name="get_chef_phone_number"),
    path('chef_phone_number/create', chefView.PhoneNumberChef, name="chef_phone_number"),
    path('chef_phone_number/<str:phone_number_id>', chefView.EditPhoneNumberChef, name="chef_phone_number"),
    path('chef_phone_number/<str:phone_number_id>/remove', chefView.RemovePhoneNumberChef, name="remove_chef_phone_number"),
    path('get_address', chefView.GetAddress, name="get_address"),
    path('create_address', chefView.CreateAddress, name="create_address"),
    path('edit_address/<str:addresss_id>', chefView.EditAddress, name="edit_address"),
    path('delete_address/<str:addresss_id>', chefView.DeleteAddress, name="delete_address"),
    

    #User
    path('user', regularUserView.HomePage, name="user_home"),
    path('user_register', homeView.RegularUserRegister, name="user_register"),
    path('user_edit', regularUserView.EditRegularUser, name="edit_user"),
    path('user_image', regularUserView.ImageRegularUser, name="user_image"),
    path('user_image', regularUserView.RemoveImageRegularUser, name="remove_user_image"),


    #Recipe
    path('create_recipe', recipeView.CreateRecipe, name="create_recipe")
=======
    path('chef_home', chefView.HomePage, name="chef_home"),
    path('chef_register', homeView.GetChefRegister, name="chef_register"),
    path('post_chef_register', homeView.PostChefRegister, name="post_chef_register"),
    path('edit_chef', chefView.GetEditChef, name="edit_chef"),
    path('post_edit_chef', chefView.PostEditChef, name="post_edit_chef"),
    path('edit_chef_image', chefView.GetImageChef, name="edit_chef_image"),
    path('post_edit_chef_image', chefView.PostImageChef, name="post_edit_chef_image"),
    path('remove_edit_chef_image', chefView.RemoveImageChef, name="remove_edit_chef_image"),

    #User
    path('user_home', regularUserView.HomePage, name="user_home"),
    path('user_register', homeView.GetRegularUserRegister, name="user_register"),
    path('post_user_register', homeView.PostRegularUserRegister, name="post_user_register"),
    path('edit_user', regularUserView.GetEditRegularUser, name="edit_user"),
    path('post_edit_user', regularUserView.PostEditRegularUser, name="post_edit_user"),
    path('edit_user_image', regularUserView.GetImageRegularUser, name="edit_user_image"),
    path('post_user_chef_image', regularUserView.PostImageRegularUser, name="post_edit_user_image"),
    path('remove_user_chef_image', chefView.RemoveImageChef, name="remove_edit_user_image")
>>>>>>> parent of d3149f3... worked on upload muiltiple feature image for chef
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)