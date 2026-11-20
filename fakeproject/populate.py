import os
import django
from decimal import Decimal


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakeproject.settings')
django.setup()
from faker import Faker
from myapp.models import Employee
f=Faker('en_IN')

def generate_populate(n):
    for i in range(n):
        fname=f.name()
        fage=f.random_int(min=20,max=50)
        femail=f.email()
        fsalary=Decimal(f.random_int(min=20000,max=50000))
        e=Employee.objects.get_or_create(name=fname,age=fage,email=femail,salary=fsalary)


generate_populate(20)


