"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from fourthapp import views
from fourthapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('car/<int:pk>/', car, name = 'car'),
    path('cartype/<int:pk>/', cartype, name = 'cartype'),
    path('add_country/', add_country, name='add_country'),
    path('test', test),
    path('add_car_model/', add_car_model, name='add_car_model'),
    path('add_car/', add_car, name='add_car'),
    path('update_car/<int:pk>/', update_car, name = 'update_car'),
    path('detail_car/<int:pk>/', detail_car, name = 'detail_car'),
    path('del_car/<int:pk>/', del_car, name = 'del_car'),
]
