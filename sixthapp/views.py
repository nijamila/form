from django.shortcuts import render
from django.http import HttpResponse

def car(request):
    return HttpResponse('porsche')

def spf(request):
    return HttpResponse('korean')

def lipstick(request):
    return HttpResponse('jeoseon')
