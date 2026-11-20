from django.shortcuts import render

from myapp.models import studentdata

# Create your views here.
def data(request):
    s=studentdata.objects.all()
    ctx={'stu':s}
    return render(request,'stu.html',ctx)