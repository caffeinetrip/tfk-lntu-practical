from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
]