from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from products.models import Product

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Card Number', required=True)
    expiration_date = forms.CharField(label='Expiration Date (MM/YY)', required=True)
    cvc = forms.CharField(label='CVC', required=True)

    stripeToken = forms.CharField(label='Stripe Token', required=True, widget=forms.HiddenInput())
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit Payment'))
