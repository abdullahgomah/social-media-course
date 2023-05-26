from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150) 
    email = models.EmailField(max_length=255, unique=True) 

    def __str__(self):
        return self.name 