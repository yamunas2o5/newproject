from django.shortcuts import render
from myapp.models import Employee

# Create your views here
def employee_list(request):     
    e = Employee.objects.all()
    ctx = {'employees': e}
    return render(request, 'employee.html', ctx)


