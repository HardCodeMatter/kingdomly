from django.db import models


class Country(models.Model):
    name = models.CharField(('Name'), max_length=100)
    capital = models.CharField(('Capital'), max_length=100)
    continent = models.CharField(('Continent'), max_length=100, blank=True, null=True)
    region = models.CharField(('Region'), max_length=100, blank=True, null=True)
    largest_city = models.CharField(('Largest city'), max_length=100, blank=True, null=True)
    area = models.IntegerField(('Area'), blank=True, null=True)
    population = models.IntegerField(('Population'), blank=True, null=True)
    density = models.FloatField(('Density'), blank=True, null=True)
    gross_product = models.IntegerField(('Gross product'), blank=True, null=True)
    currency = models.CharField(('Currency'), max_length=50, blank=True, null=True)
    calling_code = models.IntegerField(('Calling code'), blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.pk})'

    def get_population(self):
        return f'{self.population:,}'

    def get_area(self):
        return f'{self.area:,}'
