from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categorys = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categorys]

        self.fields['category'].choices = friendly_names

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'name',
            'description',
            'category',
            'price',
            'image',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
