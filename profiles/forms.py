from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country',
        ]
        labels = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Post Code',
            'default_country': 'Country',
        }
        widgets = {
            'default_country': forms.Select(),
        }