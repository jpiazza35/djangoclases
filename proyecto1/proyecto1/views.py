from django.http import HttpResponse
from django.template import Template
from django.template.context import Context
from django.template import loader  ## importamos loaders para cargar plantillas mas rapido
from datetime import datetime


def saluda(req):
    return HttpResponse("Hola a todos que rapido es codear en django")


def despedirse(req):
    HttpResponse(
        """
        <h1>Adios , me fui</h1>
        """
    )

def saludar_nombre(req, nombre):
    texto = f'Hola {nombre} como estas?'
    return HttpResponse(texto)

def aneo(req, nacimiento):
    today = datetime.today().year
    print(today)
    your_age = today - int(nacimiento)
    texto = f'you are {your_age} old'
    return HttpResponse(texto)


def template(req):
    mi_dict = {
        "nombre": "Jose",
        "Apellido": "Piazza",
        "hoy": datetime.now(),
        "notas": [3,4,10]

    }
     
    '''
    forma antigua de pasar info a las plantillas
    miHtml = open('/Users/jpiazza/courses/coderhouse/djangoclases/proyecto1/proyecto1/plantillas/template1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(mi_dict)
    documento = plantilla.render(miContexto)
    '''
    ##usando loader es mucho mas simple 
    mi_plantilla = loader.get_template('template1.html')
    documento = mi_plantilla.render(mi_dict)
    return HttpResponse(documento)
