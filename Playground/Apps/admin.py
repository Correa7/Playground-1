from django.contrib import admin

from Apps.models import Curso, Entregable, Estudiante, Profesor

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)