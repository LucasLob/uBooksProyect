from django import forms
from books.models import Libro


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        exclude = ['creado_por', 'unidades', 'veces_vendido']