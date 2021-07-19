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
from chef_management_app.views import loginView
from chef_management_app.views import adminView
from chef_management_app.views import chefView
from chef_management import settings


urlpatterns = [
    path('', homeView.HomePage),
    path('admin/', admin.site.urls),

    #Login
    path('login', loginView.GetLogin, name="login"),
    path('postlogin', loginView.PostLogin, name="postlogin"),
    path('logout', loginView.LogOut, name="logout"),

    #Admin
    path('admin', adminView.HomePage, name="admin"),
 
    #Chef
    path('chef_register', chefView.GetRegister, name="chef_register"),
    path('post_chef_register', chefView.PostRegister, name="post_chef_register")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
