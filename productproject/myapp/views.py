from django.shortcuts import render

from myapp.models import Product

# Create your views here.
def product_list(request):
    p=Product.objects.all()
    d={
        'prod':p
    }
    return render(request, 'product.html',d)

