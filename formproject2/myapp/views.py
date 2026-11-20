from django.shortcuts import render
from myapp.forms import StudentForm
from myapp.models import Student

# Create your views here.
def formview(request):
    f=StudentForm()
    if request.method=="POST":
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save()
            s=Student.objects.all()
            d={'stud':s}
            # name=f.cleaned_data['name']
            # age=f.cleaned_data['age']
            # email=f.cleaned_data['email']
        # d={'name':name,'age':age,'email':email}
        # return render(request,'output.html',d)
            return render(request,'1.html',d)
    
    d={'form':f}
    return render(request,'form.html',d)
        

