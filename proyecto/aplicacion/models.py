from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class tipo_medio(models.Model):
    cod_tipo_medio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)



class medio(models.Model):
    cod_medio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo_medio = models.ForeignKey(tipo_medio,null=True,blank=True,on_delete=models.CASCADE)
    
class periodista(models.Model):
    rut = CharField(max_length=13,primary_key=True)
    nombre = CharField(max_length=35)
    apellido_paterno = CharField(max_length=30)
    apellido_materno = CharField(max_length=30)
    correo = EmailField(max_length=40)
    password = CharField(max_length=20)

class posee(models.Model):
    periodista = ForeignKey(periodista,null=True,blank=True,on_delete=models.CASCADE)
    medio = ForeignKey(medio,null=True,blank=True,on_delete=models.CASCADE)

class competencia(models.Model):
    cod_competencia = IntegerField(primary_key=True)
    nombre = CharField(max_length=80)

class publicacion(models.Model):
    cod_publicacion = IntegerField(primary_key=True)
    titulo = CharField(max_length=50)
    descripcion = CharField(max_length=600)
    idioma = CharField(max_length=100)
    fecha_publicacion = DateField()
    periodista = ForeignKey(periodista,null=True,blank=True,on_delete=models.CASCADE)
    competencia = ForeignKey(competencia,null=True,blank=True,on_delete=models.CASCADE)