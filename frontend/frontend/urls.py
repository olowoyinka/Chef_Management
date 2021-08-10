"""frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mCode import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Guest 
    path('', views.guest_home, name="guest_home"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('vendor-register', views.vendor_register, name="vendor-register"),

    #Chef 
    path('chef/dashboard', views.chef_home, name="chef-home"),
    path('chef/new', views.new_recipe, name="new-recipe"),
    path('chef/recipe', views.recipe, name="recipe"),
    path('chef/update', views.update_delete, name="update recipe"),
    path('chef/customer_feedback', views.customer_feedback, name="customerfeedback"),
]

urlpatterns += staticfiles_urlpatterns()