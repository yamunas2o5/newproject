from django.shortcuts import render,redirect
from myapp.models import Product
from myapp.models import ProductForm


def home(request):
    photos = Product.objects.all()
    ctx = {'pho': photos}
    return render(request, 'index.html', ctx)

def createproduct(request):
    f=ProductForm()
    if request.method=="POST":
        f=ProductForm(request.POST,request.FILES)
        if f.is_valid():
            f.save(commit=True) 
        return redirect('display')
    d={'form':f}
    return render(request,'insertion.html',d)    