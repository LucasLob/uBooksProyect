from django.shortcuts import render
from django.http import HttpResponse
from libros.models import Libro

def home(request):
    libros = Libro.objects.all()
    context = {
        'libros_list': libros
    }
    return render(request, 'libros/index.html',context)