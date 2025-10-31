from django.contrib import admin
from .models import *

class CarAdmin(admin.ModelAdmin):
    list_display=('title', 'model', 'country', 'colour')
    list_display_links = ['title']
    search_fields = ['title']

admin.site.register(Car, CarAdmin)

class CartypesAdmin(admin.ModelAdmin):
    # list_display=('title')
    # list_display_links = ['title']
    search_fields = ['title']
    # list_editable = ['']

admin.site.register(Cartype, CartypesAdmin)

class CountryAdmin(admin.ModelAdmin):
    # list_display=('title')
    # list_display_links = ['title']
    search_fields = ['title']
    # list_editable = ['']

admin.site.register(Country, CountryAdmin)