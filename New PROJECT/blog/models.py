from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name