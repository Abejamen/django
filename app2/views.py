from django.shortcuts import render
from django.http import HttpResponse

# Create youfrom django.http import HttpResponse

def vista1(request):
    return HttpResponse("<h1>App2 - Vista1</h1><p> Hola desde app2/Vista1</p>")

def vista2(request):
    return HttpResponse("<h1>App2 - Vista2</h1><p> Hola desde App2/Vista2</p>")