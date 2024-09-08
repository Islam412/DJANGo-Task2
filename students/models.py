from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    img = models.ImageField(upload_to='student')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
