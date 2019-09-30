from django.db import models
class Fake(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    city=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)

# Create your models here.
