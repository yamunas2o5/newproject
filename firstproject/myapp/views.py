from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    a="Welcome to Django Session"
    return HttpResponse(a)

def view2(request):
    b="Welcome to Django Session 2"
    return HttpResponse(b)