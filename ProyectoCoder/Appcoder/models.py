from django.db import models

# Create your models here.

##Aqui se crean las estructuras de nuestras bases de datos. un modelo es una clase que luego se crearan instancias de model

class Curso(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    fecha_ingreso = models.DateField('fecha',auto_now=False, auto_now_add=False)

class Profesor(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    fecha_ingreso = models.DateField('fecha',auto_now=False, auto_now_add=False)
    email = models.CharField('email', max_length=50 )

class Entregable(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

