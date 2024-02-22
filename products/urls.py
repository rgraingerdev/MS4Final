from django.urls import path
from . import views
from bag.views import add_to_bag

urlpatterns = [
    path('', views.product_list, name='products'),
]
