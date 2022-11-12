from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # path('', views.index , name="index"),
    path('', views.signin , name="signin"),

    path('signup', views.signup , name="signup"),
    path('signout', views.signout , name="signout"),
    path('signin', views.signin , name="signin"),
    path('activate/<uidb64>/<token>', views.activate , name="activate"),
]