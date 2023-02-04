from django.contrib import admin
from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'continent', 'region', 'currency',)
    list_filter = ('name', 'capital', 'continent', 'region', 'currency',)

    fieldsets = (
        ('Country information', {'fields': (
            'name', 'capital', 'largest_city', 'continent', 'region', 'flag',
        )}),
        ('Territory information', {'fields': (
            'area', 'population', 'density', 'demonym',
        )}),
        ('Economy information', {'fields': (
            'gross_product', 'per_capita', 'currency',
        )}),
        ('Technical information', {'fields': (
            'calling_code', 'domain',
        )}),
    )

    search_fields = ('name', 'capital', 'continent', 'region', 'currency', 'calling_code',)
    ordering = ('-id',)
