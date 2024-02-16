"""
URL configuration for megashop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import homepage, signup_view
from basket.views import basket, add_to_basket
from products.views import products, add_product, edit_product, delete_product

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('sign-up/', signup_view, name='signup_view'),
    path('', homepage, name='homepage'),
    path('basket', basket, name='basket'),
    path('basket/add_to_basket<int:product_id>/', add_to_basket, name='add_to_basket'),
    path("products/", products, name='products'),
    path("products/add_product/", add_product,  name='add_product'),
    path("products/<int:product_id>/edit/", edit_product,  name='edit_product'),
    path("products/<int:product_id>/delete_product/", delete_product,  name='delete_product'),

]
