from django import forms
from .models import Country


class CountryCreateForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            'name', 'capital', 'continent', 'region', 'largest_city',
            'area', 'population', 'density', 
            'gross_product', 'currency', 'calling_code',
        )
