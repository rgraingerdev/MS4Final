# urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('payment/', views.payment, name='payment'),
    path('process_payment/<str:client_secret>/', views.process_payment, name='process_payment'),
]
