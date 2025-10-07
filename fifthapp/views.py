from django.shortcuts import render
from django.http import HttpResponse

def hobby1(request):
    return HttpResponse('sleeping')

def hobby2(request):
    return HttpResponse('reading')

def hobby3(request):
    return HttpResponse('uno')
