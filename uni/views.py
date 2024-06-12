from django.shortcuts import get_object_or_404, render, redirect

from uni.forms import AlumnoForm, AlumnoMatriculaForm
from uni.models import Carrera

# Create your views here.

def matricularAlumno(request):
    if request.method == 'POST':
        formAlumno = AlumnoMatriculaForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('index')
    else:
        formAlumno = AlumnoMatriculaForm()
    return render(request, 'alumnos/matricula.html', {'formAlumno': formAlumno})

def nuevoAlumno(request, id):
    if request.method == 'POST':
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            nuevo = formAlumno.save(commit=False)
            carrera = get_object_or_404(Carrera, pk=id)
            nuevo.carrera = carrera
            nuevo.save()
            return redirect('carreras')
    else:
        formAlumno = AlumnoForm()
    return render(request, 'alumnos/nuevo.html', {'formAlumno': formAlumno})

def verCarrera(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras/carreras.html', {'carreras': carreras})
