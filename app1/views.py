from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    return HttpResponse("<h1>App1 -Vista1</h1><p>Hola desde la app1/Vista1</p>")
def vista2(request):
    return HttpResponse("<h1>App1 - Vista2</h1><p>Holas desde App1/Vista2<(/p>)")
