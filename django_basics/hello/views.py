from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def evgenii(request):
    return HttpResponse("Hello, Evgenii!")