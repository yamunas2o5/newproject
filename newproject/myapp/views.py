from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def aboutUs(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')
