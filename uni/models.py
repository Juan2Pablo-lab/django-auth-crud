from django.db import models

# Create your models here.

I, II, III, IV, V, VI, VII, VIII, IX, X = 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'

CICLOS = [
    (I, 'Primer Ciclo'), 
    (II, 'Segundo Ciclo'), 
    (III, 'Tercer Ciclo'), 
    (IV, 'Cuarto Ciclo'), 
    (V, 'Quinto Ciclo'), 
    (VI, 'Sexto Ciclo'),
    (VII, 'Septimo Ciclo'),
    (VIII, 'Octavo Ciclo'),
    (IX, 'Noveno Ciclo'),
    (X, 'Decimo Ciclo')
]


class Carrera(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    duracion = models.CharField(max_length=5)
    def __str__(self):
        return f'{self.nombre}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    dni = models.IntegerField(unique=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    dni = models.IntegerField(unique=True)
    ciclo = models.CharField(choices=CICLOS, max_length=5, default=I)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    ciclo = models.CharField(choices=CICLOS, max_length=5, default=I)
    fechacompletada = models.DateTimeField(null=True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nombre} {self.carrera}'
