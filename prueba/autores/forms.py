

from django import forms
from .models import Autores

#Crear formulario
class AutorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Autores

        #especificar los campos
        fields = [
            'nombre',
            'apellido',
            'pais'
        ]