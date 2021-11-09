from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    return render(request, 'products.html')


