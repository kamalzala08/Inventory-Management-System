from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name='user/signin.html'), name="signin"),    
    path('logout', auth_view.LogoutView.as_view(template_name='user/logout.html'), name="logout"), 
    path('signup', views.signup, name="signup"),    
    path('profile', views.profile, name="profile"),    
    path('updateprofile', views.updateprofile, name="updateprofile"),    
 ]
