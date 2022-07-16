from tkinter import CASCADE
from django.db import models
from usuarios.models import users

# Create your models here.

class carros(models.Model):
    marca = models.CharField(blank=False, null=False, max_length=50)
    modelo = models.CharField(blank=False, null=False, max_length=50)
    color = models.CharField(blank=False, null=False, max_length=10)
    potencia = models.IntegerField(blank=False, null=False)
    año = models.IntegerField(blank=False, null=False)
    placa = models.CharField(blank=False, null=False, max_length=10)
    propietario = models.ForeignKey(users, on_delete=models.CASCADE)