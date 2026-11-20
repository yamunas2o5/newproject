from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='emp_images/')

def __str__(self):
    return self.name
