from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomSignUpForm, ProfileForm
from allauth.account.views import SignupView
from django.contrib.auth.models import User
from .models import Profile

class CustomSignUpView(SignupView):
    template_name = 'signup.html'
    form_class = CustomSignUpForm

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            if profile is None:
                form.instance.user = request.user
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'profile':profile, 'form':form})