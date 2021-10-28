from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filters import StyleFilter

# Create your views here.

def filter(request):
    return HttpResponse("Hiiiiiiii")