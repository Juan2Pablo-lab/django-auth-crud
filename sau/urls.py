"""
URL configuration for sau project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import bienvenido, Registro, iniciarSesion, cerrarSesion
from uni.views import verCarrera, nuevoAlumno, matricularAlumno

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", bienvenido, name='index'),
    path("carreras/", verCarrera, name='carreras'),
    path("matricular/", matricularAlumno, name='matricular'),
    path("carrera/<int:id>", nuevoAlumno, name='nuevo_alumno'),
    path("registro/", Registro, name='registro'),
    path("ingresar/", iniciarSesion, name='ingresar'),
    path("cerrar/", cerrarSesion, name='cerrar'),
]
