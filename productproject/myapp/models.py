from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    material=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    description=models.TextField() #huge content
    image=models.ImageField(upload_to='products/')

def __str__(self):
    return self.name



