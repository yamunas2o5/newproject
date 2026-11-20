from django.db import models


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    
