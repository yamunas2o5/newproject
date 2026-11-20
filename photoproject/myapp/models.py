from django.db import models

class Gallery(models.Model):
    event_name = models.CharField(max_length=50)
    description = models.TextField()
    event_date = models.DateField()
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.event_name