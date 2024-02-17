"""
URL configuration for basket project.

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

from django.urls import path
from .views import basket, add_to_basket,clear_basket


urlpatterns = [
    path('basket/', basket, name='basket'),
    path('basket/add_to_basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('basket/clear_basket', clear_basket, name='clear_basket'),
]
