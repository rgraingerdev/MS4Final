from django.urls import path
from .views import payment

urlpatterns = [
    path('checkout/', payment, name='payment')
]