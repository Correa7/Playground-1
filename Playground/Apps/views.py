from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader
from Apps import Template
from Apps.models import Curso, Estudiante, Profesor, Entregable
from Apps.forms import CursoFormulario
def inicio (request):

    return render(request, "inicio.html")

def cursos (request):

    return render(request, "curso.html")

def profesores (request):

    return render(request, "profesor.html")

def estudiantes (request):

    return render(request, "estudiante.html")

def entregables (request):

    return render(request, "entregable.html")

# def cursoFormulario (request):

#     if request.method == "POST":

#         curso = Curso(nombre = request.POST["nombre"], camada = request.POST["camada"])

#         curso.save()

#         return render (request, "inicio.html")

#     return render (request, "cursoFormulario.html")


def cursoFormulario (request):

    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            data = miFormulario.cleaned_data

            curso = Curso(nombre = data["curso"], camada = data["camada"])

            curso.save()

            return render (request, "inicio.html")

    else:

        miFormulario = CursoFormulario()    

    return render (request, "cursoFormulario.html", {"miFormulario" : miFormulario})


def busquedaCamada (request):

    return render (request, "busquedaCamada.html")


def buscar (request):

    if request.GET["camada"]:

        camada= request.GET["camada"]
        cursos= Curso.objects.filter(camada__icontains=camada)

        return render(request, "resultadoDeBusqueda.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta ="No enviaste datos"

    return HttpResponse (respuesta)