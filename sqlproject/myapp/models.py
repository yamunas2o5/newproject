from django.db import models

# Create your models here.
class studentdata(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    place=models.CharField(max_length=30)
    email = models.EmailField()

def __str__(self):
    return self.name