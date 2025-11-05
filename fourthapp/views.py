from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView, ListView
from fourthapp.forms import CartForm, CarForm, CounForm
from fourthapp.models import Cartype, Car, Country
from django.shortcuts import render, redirect
from .models import Cartype, Country
from .forms import CartForm, CounForm

# def index(request):
#     cartype = Cartype.objects.all()
#     country = Country.objects.all()
#     cars = Car.objects.all()
#
#     car_form = CartForm(request.POST or None)
#     country_form = CounForm(request.POST or None)
#
#     if request.method == 'POST':
#         if 'add_car' in request.POST and car_form.is_valid():
#             car_form.save()
#             return redirect('index')
#         if 'add_country' in request.POST and country_form.is_valid():
#             country_form.save()
#             return redirect('index')
#
#     return render(request, 'index.html', {
#         'cartype': cartype,
#         'country': country,
#         'cars': cars,
#         'car_form': car_form,
#         'country_form': country_form
#     })

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

# def add_country(request):
#     if request.method == 'POST':
#         form = CounForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CounForm()
#     return render(request,'country.html', {'form': form})

class CreateCountry(CreateView):
    form_class = CounForm
    template_name = 'country.html'
    success_url = reverse_lazy('index')

def add_car_model(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CartForm()
    return render(request,'model.html', {'form': form})

# def add_car(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CarForm()
#     return render(request,'car.html', {'form': form})

class CreateCar(CreateView):
    form_class = CarForm
    template_name = 'car.html'
    success_url = reverse_lazy('index')


# def detail_car(request, pk):
#     car = get_object_or_404(Car, id=pk)
#     context = {
#         'car': car
#     }
#
#     return render(request, 'detail_new.html', context = context)

class ViewCars(DetailView):
    model = Car
    context_object_name = 'cars'
    template_name = 'detail_new.html'
    pk_url_kwarg = 'pk'

# def update_car(request, pk):
#     car = Car.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = CarForm(request.POST, instance = car)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CarForm(instance=car)
#     context = {
#         'form': form,
#         'car': car
#     }
#
#     return render(request, 'update.html', context=context)

class CarUpdate(UpdateView):
    form_class = CarForm
    template_name = 'update.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'



# def del_car(request, pk):
#     car = Car.objects.get(pk=pk)
#     car.delete()
#     cars = Car.objects.all()
#     cartype = Cartype.objects.all()
#     context = {
#         'cars': cars,
#         'cartype': cartype,
#         'title': "Cars Title"
#     }
#
#     return render(request, 'index.html', context = context)

class DeleteCar(DeleteView):
    model = Car
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'

class CarByType(ListView):
    model = Cartype
    template_name = 'index.html'
    context_object_name = 'cars'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartype'] = Cartype.objects.all()
        return context

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Car.objects.filter(category_type_id=pk)
        return Car.objects.all()