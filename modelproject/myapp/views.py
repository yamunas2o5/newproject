from django.shortcuts import render

from myapp.models import Student

# Create your views here.
def data(request):
    s=Student.objects.all()#connect the db to the views
    ctx={'stud':s}
    return render(request, 'myapp/index.html', ctx)
