from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [    
    path("register", register, name="Register"),
    path("login", login_request, name="Login"),
    path("profile-edit", profileEdit, name="Profile Edit"),
    path("logout", LogoutView.as_view(template_name="users/logout.html"), name="Logout")
]