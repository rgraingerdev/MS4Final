from django import forms

class AddToBasketForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
