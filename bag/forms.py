from django import forms

class AddToBagForm(forms.Form):
    quatity = forms.IntegerField(min_value=1, initial=1,widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'})),