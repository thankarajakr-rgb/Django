from django.db import models

# Create your models here

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Course=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    