from django.db import models

# Create your models here.

class users(models.Model):
    nombre = models.CharField(max_length=50)
    num = models.IntegerField()
    sexo = models.CharField(max_length=50)
    edad = models.IntegerField()