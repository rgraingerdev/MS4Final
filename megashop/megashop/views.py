from django.shortcuts import render
from .forms import CustomSignUpForm
from allauth.account.views import SignupView

def homepage(request):
    return render(request, './megashop/landing.html')

class CustomSignUpView(SignupView):
    form_class = CustomSignUpForm
    template_name = 'megashop/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
signup_view = CustomSignUpView.as_view()