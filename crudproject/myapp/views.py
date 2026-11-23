# from django.shortcuts import render,redirect
# from myapp.models import Product
# from myapp.models import ProductForm


# def home(request):
#     photos = Product.objects.all()
#     ctx = {'pho': photos}
#     return render(request, 'index.html', ctx)

# def createproduct(request):
#     f=ProductForm()
#     if request.method=="POST":
#         f=ProductForm(request.POST,request.FILES)
#         if f.is_valid():
#             f.save(commit=True) 
#         return redirect('display')
#     d={'form':f}
#     return render(request,'insertion.html',d)    


from django.shortcuts import render,redirect
from myapp.models import Product
from myapp.forms import ProductForm

# Create your views here.
def home(request):
    photos=Product.objects.all()
    ctx={'photos':photos}
    return render(request,'index.html',ctx)

def display(request):
    photos=Product.objects.all()
    search = request.GET.get('search')
    if search:
        p=Product.object.filter(name__icontains=search)
    d={'photos':photos}
    return render(request,'index.html',d)

def createproduct(request):
    f=ProductForm()
    if request.method=='POST':
        f=ProductForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
        return redirect('display')
    d={'form':f}
    return render(request, 'insertion.html', d)



def updateproduct(request, id):
    photos=Product.objects.get(id=id)
    f=ProductForm(instance=photos)
    if request.method=='POST':
        f=ProductForm(request.POST, request.FILES, instance=photos)
        if f.is_valid():
            f.save()
        return redirect('display')
    d={'form':f}
    return render(request, 'insertion.html', d)

def deleteproduct(request, id):
    photos=Product.objects.get(id=id)
    photos.delete()
    return redirect('display')