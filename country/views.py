from django.shortcuts import render, redirect
from .forms import CountryCreateForm


def index(request):
    return render(request, 'country/base.html', {})

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
