from django.shortcuts import render, redirect
from django.http import HttpResponse

from fourthapp.forms import CartForm, CarForm, CounForm
from fourthapp.models import Cartype, Car, Country



from django.shortcuts import render, redirect
from .models import Cartype, Country
from .forms import CartForm, CounForm

def index(request):
    cartype = Cartype.objects.all()
    country = Country.objects.all()

    car_form = CartForm(request.POST or None)
    country_form = CounForm(request.POST or None)

    if request.method == 'POST':
        if 'add_car' in request.POST and car_form.is_valid():
            car_form.save()
            return redirect('index')
        if 'add_country' in request.POST and country_form.is_valid():
            country_form.save()
            return redirect('index')

    return render(request, 'index.html', {
        'cartype': cartype,
        'country': country,
        'car_form': car_form,
        'country_form': country_form
    })

def car(request):
    car = Car.objects.all()
    context = {
        "car": car
    }
    return render(request, 'car.html', context)


def country(request):
    country = Country.objects.all()
    context = {
        "country": country
    }
    return render(request, 'country.html', context)


def cartype(request):
    cartype = Cartype.objects.all()
    # country = Country.objects.all()
    context = {
        'cartype': cartype,
        # 'country': country
    }
    return render(request, 'index.html', context)


def test(request):
    return HttpResponse('salom dunyo')


def add_car_model(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CartForm()
    return render(request,'model.html', {'form': form})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request,'car.html', {'form': form})

def add_country(request):
    if request.method == 'POST':
        form = CounForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CounForm()
    return render(request,'country.html', {'form': form})
