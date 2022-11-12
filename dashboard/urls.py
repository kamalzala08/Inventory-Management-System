from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index , name="dashboard-index"),
    path('dashboard-staff', views.staff , name="dashboard-staff"),
    path('dashboard-products', views.products , name="dashboard-products"),
    path('dashboard-orders', views.orders , name="dashboard-orders"),
    path('products/delete/<int:pk>/', views.product_delete,name='dashboard-product-delete'),
    path('products/update/<int:pk>/', views.product_update,name='dashboard-product-update'),
    path('staff-detail/<int:pk>/', views.staff_detail,name='staff-detail'),
    
 ]