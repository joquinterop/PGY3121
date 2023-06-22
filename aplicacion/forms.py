from django import forms
from django.contrib.auth.models import User
from .models import Articulo

class usuarioFormulario(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email",]
        labels = {'first_name':'Nombre',
                  'last_name':'Apellido',
                  'email':'Correo Electronico',}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }

class articuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        exclude = ('idUsuario',)
        fields = ["articulo","descripcion","imagen","estado"]
        widgets = {
            'estado': forms.TextInput(attrs={'type': 'hidden'}),
        }
