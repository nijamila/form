from django import forms
from fourthapp.models import Cartype, Car, Country


class CartForm(forms.ModelForm):
    class Meta:
        model = Cartype
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'model', 'country', 'colour', 'price', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'colour': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class CounForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
