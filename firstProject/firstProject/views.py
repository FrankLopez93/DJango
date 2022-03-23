from django.http import HttpResponse  #always import this library for views
import datetime
from django.template import Template, Context
from django.template.loader import get_template

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def gretting(request):
    p1 = Persona('Francisco', 'Lopez')
    #nombre = 'Javier'
    #apellido = 'Lopez'

    temas = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    ahora = datetime.datetime.now()
    # doc_externo = open("C:/Users/Fc/Desktop/projectsDjango/firstProject/firstProject/Templates/myTemplate.html")
    # templt = Template(doc_externo.read())
    # doc_externo.close()

    doc_externo = get_template('myTemplate.html')
    # ctx = Context({'nombre_persona':p1.nombre,'apellido':p1.apellido,'actual':ahora,'temas':temas})
    documento = doc_externo.render({'nombre_persona':p1.nombre,
                                    'apellido':p1.apellido,
                                    'actual':ahora,
                                    'temas':temas
                                })

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
