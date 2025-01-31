from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.urls import path
from django.contrib import admin


def home(request):
    return render(request, 'home.html')
def listorders(request):
    return HttpResponse("Hello, world. You're at the polls page.")

def listorders1(request):
    return HttpResponse("Hello, world. You're at the polls page1111.")

def listorders2(request):
    return HttpResponse("Hello, world. You're at the polls page222.")

def listorders3(request):
    return HttpResponse("Hello, world. You're at the polls page333.")