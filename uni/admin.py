from django.contrib import admin

from uni.models import Carrera, Profesor, Alumno, Curso

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Curso)
