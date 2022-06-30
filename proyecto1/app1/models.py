from datetime import datetime
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.db.models.deletion import CASCADE
from psycopg2 import Date

# Create your models here.
class tipo_demanda(models.Model):
    n_tipo_demanda = models.CharField(max_length=60,null=False)
    def __str__(self):
        return self.n_tipo_demanda

class tipo_comuna_dado(models.Model):
    n_tipo_comuna_dado = models.CharField(max_length=50)
    def __str__(self):
        return self.n_tipo_comuna_dado


class tipo_comuna_ante(models.Model):
    n_tipo_comuna_ante = models.CharField(max_length=50)
    def __str__(self):
        return self.n_tipo_comuna_ante


class demanda(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    fecha=models.DateField(blank=True,null=True)
    hora= models.DateField(blank=True,null=True)
    tpo_dem =models.ForeignKey(tipo_demanda,on_delete=CASCADE)
    detalle= models.CharField(max_length=1000,null=False)

    rut_dado = models.CharField(max_length=10,blank=False)
    nombre_dado=models.CharField(max_length=40)
    apellido_dado= models.CharField(max_length=40)
    telefono_dado=models.CharField(max_length=12)
    comuna_dado=models.ForeignKey(tipo_comuna_dado,on_delete=CASCADE)

    rut_dante = models.CharField(max_length=10,blank=False)
    nombre_dante=models.CharField(max_length=40)
    apellido_dante= models.CharField(max_length=40)
    telefono_dante=models.CharField(max_length=12)
    comuna_dante=models.ForeignKey(tipo_comuna_ante,on_delete=CASCADE)
    def __str__(self):
        txt = "id del caso: {0}"
        return txt.format(self.id)





# class abogado(models.Model):
#     rut=
