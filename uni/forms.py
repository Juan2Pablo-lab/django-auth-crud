from django.forms import EmailInput, ModelForm, TextInput

from uni.models import Alumno


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'email', 'dni']
        widgets = {
            'email': EmailInput(attrs={'type':'email'}),
            'dni': TextInput(attrs={'type':'number'})
        }

class AlumnoMatriculaForm(ModelForm):
    class Meta:
        model= Alumno
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'}),
            'dni': TextInput(attrs={'type':'number'})
        }
