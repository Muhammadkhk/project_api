from django.db import models

# Create your models here.

class Book(models.Model):
    url = models.CharField(max_length=150)
    image = models.ImageField('/image', null=True, blank=True)

    def __str__(self):
        return self.url