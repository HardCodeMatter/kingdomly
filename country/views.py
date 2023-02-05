from django.shortcuts import render, redirect
from .models import Country
from .forms import CountryForm


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

def country_edit(request, id):
    country = Country.objects.get(id=id)

    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES, instance=country)

        if form.is_valid():
            form.save()

            return redirect(f'/country/{country.id}')
    else:
        form = CountryForm(instance=country)

    context = {
        'form': form,
        'country': country,
    }
    
    return render(request, 'country/country_edit.html', context)

def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('/country/')
    else:
        form = CountryForm()

    context = {
        'form': form,
    }

    return render(request, 'country/country_create.html', context)
