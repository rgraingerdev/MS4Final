from django import forms

class PaymentForm(forms.Form):
    stripe_payment_method = forms.CharField(
        required = True, widget = forms.HiddenInput()
)
    card_number = forms.CharField(label = 'Card Number', required = True)
    exp_month = forms.CharField(label = 'Expiry Month', required = True)
    exp_year = forms.CharField(label = 'Expiry Year', required = True)
    cvc = forms.IntegerField(label = 'CVC', required = True)


    def clean_stripe_payment_method(self):
        stripe_payment_method = self.cleaned_data.get('stripe_payment_method')
        return stripe_payment_method