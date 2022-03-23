#always import this library for views
import datetime
from importlib.resources import contents
from django.http import HttpResponse

def gretting(request):
    title = "<html><body><h1>Hello World :D</h1></body></html>"
    return HttpResponse(title)

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
