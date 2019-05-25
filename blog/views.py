from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
def index(request):
    return HttpResponse('hello world')