
from django.urls import path
from Apps.views import buscar, busquedaCamada, cursoFormulario, inicio, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos", cursos, name= "cursos"),
    path("estudiantes", estudiantes, name="estudiantes"),
    path("profesores", profesores,name="profesores"),
    path("entregables", entregables, name="entregables"),
    path("cursoFormulario", cursoFormulario, name="cursoFormulario"),
    path("busquedaCamada", busquedaCamada, name= "busquedaCamada"),
    path("buscar", buscar, name="buscar"),
]

