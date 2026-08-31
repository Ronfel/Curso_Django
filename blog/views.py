from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return HttpResponse('blog do app')

def exemplo(request):
    return HttpResponse('exemplo do app')