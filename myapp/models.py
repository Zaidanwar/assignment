from django.db import models

# Create your models here.
class Register(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    gender = models.BooleanField(default=True)