from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World, you are at the polls index_Doofie Burger Supreme')
# Create your views here.
