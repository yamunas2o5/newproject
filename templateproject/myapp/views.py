from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myview(request):
    return render(request,'myapp/index.html')

def index1(request):
    return render(request, 'myapp/index1.html')

def sample(request):
    a="Yamuna"
    b=22

    return HttpResponse(f"my name is {a} and my age is {b}")


