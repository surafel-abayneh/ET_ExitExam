from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department  = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_num= models.CharField(max_length=10, blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)