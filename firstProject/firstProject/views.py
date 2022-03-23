#always import this library for views
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def gretting(request):
    p1 = Persona('Francisco', 'Lopez')
    #nombre = 'Javier'
    #apellido = 'Lopez'
    ahora = datetime.datetime.now()
    doc_externo = open("C:/Users/Fc/Desktop/projectsDjango/firstProject/firstProject/Templates/myTemplate.html")
    templt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({'nombre_persona':p1.nombre, 'apellido':p1.apellido, 'actual':ahora})
    documento = templt.render(ctx)

    return HttpResponse(documento)

def fired(request):
    return HttpResponse("Good bye world")

def todayIs(request):
    fecha = datetime.datetime.now()
    contents = """
    <html>
    <body>
    <h1>
        Date and Time %s
    </h1>
    </body>
    </html>""" % fecha

    return HttpResponse(contents)

def edad(request, e_dad, year):
    #edadActual = 29
    periodo = year - 2022
    edadFutura = e_dad + periodo
    contenido = """
    <html>
    <body>
    <h1>
        En el año %s tendrás %s años
    </h1>
    </body>
    </html>""" %(year, edadFutura)

    return HttpResponse(contenido)
