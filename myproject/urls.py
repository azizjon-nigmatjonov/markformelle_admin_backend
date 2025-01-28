"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from . import post

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", views.get_users, name="get_users"),
    path("login", views.login, name="login"),
    path("user-rolls", views.get_user_rolls, name="get_user_rolls"),
    path("rolls", views.get_rolls, name="get_rolls"),
    path("rolls/<str:roll_id>", views.get_roll, name="get_roll"),
    path("add-roll/", post.add_roll, name="add_roll"),
    path("rolls/<str:roll_id>", post.update_roll, name="update_roll"),
    path("add-user", post.add_user, name="add_user"),
    path("update-user/<str:user_id>", post.update_user, name="update_roll"),
    path("translations", views.get_translations, name="get_translations"),
    path("add-translations", post.add_translations, name="add_translations"),
]
