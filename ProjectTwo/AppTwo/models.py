from django.db import models

# Create your models here.
class user(models.Model):
    firstName=models.CharField(max_length=246)
    lastName=models.CharField(max_length=246)
    Email=models.EmailField(max_length=256,unique=True)
