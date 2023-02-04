from django import forms
from .models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            'name', 'capital', 'continent', 'region', 'largest_city',
            'flag',
            'area', 'population', 'density', 'demonym', 
            'gross_product', 'per_capita', 'currency',
            'calling_code', 'domain',
        )
