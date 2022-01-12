from Appcoder.models import Curso
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def crea_curso(self, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return  HttpResponse(f'se creo el curso de {nombre} con la camada {camada}')