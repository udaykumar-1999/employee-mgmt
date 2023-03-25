from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()