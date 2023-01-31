from django.contrib import admin
from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'continent', 'region', 'currency',)
    list_filter = ('name', 'capital', 'continent', 'region', 'currency',)

    fieldsets = (
        ('Country information', {'fields': (
            'name', 'capital', 'largest_city', 'continent', 'region',
        )}),
        ('Territory information', {'fields': (
            'area', 'population', 'density',
        )}),
        ('Value information', {'fields': (
            'gross_product', 'currency', 'calling_code',
        )}),
    )

    search_fields = ('name', 'capital', 'continent', 'region', 'currency', 'calling_code',)
    ordering = ('name',)
