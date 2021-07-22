from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "chef_management_app.views.adminView":
                    pass
                elif modulename == "chef_management_app.views.homeView":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "chef_management_app.views.chefView":
                    pass
<<<<<<< HEAD
                elif modulename == "chef_management_app.views.recipeView":
                    pass
                elif modulename == "chef_management_app.views.homeView" or modulename == "django.views.static":
=======
                elif modulename == "chef_management_app.views.homeView":
>>>>>>> parent of d3149f3... worked on upload muiltiple feature image for chef
                    pass
                else:
                    return HttpResponseRedirect(reverse("chef_home"))
            elif user.user_type == "3":
                if modulename == "chef_management_app.views.regularUserView":
                    pass
                elif modulename == "chef_management_app.views.homeView":
                    pass
                else:
                    return HttpResponseRedirect(reverse("user_home"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse("postlogin"):
                pass
            else:
                return HttpResponseRedirect(reverse("login"))