from django.shortcuts import render, redirect
from .models import Country
from .forms import CountryCreateForm


def index(request):
    return render(request, 'country/base.html', {})

def country_list(request):
    countries = Country.objects.all().order_by('name')

    context = {
        'countries': countries,
    }

    return render(request, 'country/country_list.html', context)

def country_detail(request, id):
    country = Country.objects.get(id=id)

    context = {
        'country': country
    }

    return render(request, 'country/country_detail.html', context)

def country_create(request):
    if request.method == 'POST':
        form = CountryCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/country/')
    else:
        form = CountryCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'country/country_create.html', context)
