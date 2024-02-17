from django.contrib import admin
from django.urls import path, include
from .forms import CustomSignUpForm
from allauth.account.views import SignupView


class CustomSignUpView(SignupView):
    template_name = 'signup.html'
    form_class = CustomSignUpForm