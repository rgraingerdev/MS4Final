from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomSignUpForm, ProfileForm
from allauth.account.views import SignupView


class CustomSignUpView(SignupView):
    template_name = 'signup.html'
    form_class = CustomSignUpForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form':form})