from django import forms

class AddToBagForm(forms.Form):
    quatity = forms.IntegerField(min_value=1),