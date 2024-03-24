from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    coutry = models.CharField(max_length=50)