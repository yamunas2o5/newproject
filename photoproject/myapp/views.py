from django.shortcuts import render
from myapp.models import Gallery

# Create your views here.
def home(request):
    photos=Gallery.objects.all()
    ctx={'pho':photos}
    return render(request,'index.html',ctx)
