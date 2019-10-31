from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home/home_base.html')

