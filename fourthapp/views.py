from django.shortcuts import render
from django.http import HttpResponse

def classes(request):
    return HttpResponse('11')

def major(request):
    return HttpResponse('computer science')

def cat(request):
    return HttpResponse('kitty')
