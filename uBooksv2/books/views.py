import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from books.forms import LibroForm
from books.models import Libro


def home(request):
    libros = Libro.objects.all().order_by('-veces_vendido')

    ultimos_libros = Libro.objects.all().order_by('-momento_creacion')

    libros_actuales = Libro.objects.filter(aniolanzamiento="2018")

    context = {
        'lista_libros': libros[:9],
        'ultimos_libros': ultimos_libros[:9],
        'actualidad': libros_actuales[:9],
    }

    return render(request, 'books/index.html', context)


def detalle(request, pk):
    libros = Libro.objects.filter(pk=pk)

    libro = libros[0] if len(libros) == 1 else None

    if libro is not None:
        # Plantilla
        context = {
            'libro': libro,
        }
        return render(request, 'books/detalle.html', context)

    else:
        return HttpResponseNotFound("El producto que desea acceder no existe...")

@login_required
def crear_libro(request):
    mensaje = ""
    if request.method == "GET":
        form = LibroForm()
    else:
        libro_creado_por = Libro()
        libro_creado_por.creado_por = request.user
        form = LibroForm(request.POST, instance=libro_creado_por)
        if form.is_valid():
            nuevo_libro = form.save()
            form = LibroForm()
            mensaje = "El libro se ha guardado correctamente."
            time.sleep(2)
            return redirect('inicio')

    context = {
        'libro_form': form,
        'mensaje': mensaje
    }
    return render(request, 'books/crearlibro.html', context)

def listado_libros(request):
    if request.user.is_superuser:
        libros = Libro.objects.all()
    else:
        libros = Libro.objects.filter(creado_por=request.user)

    context = {
        'mislibros': libros
    }

    return render(request, 'books/mislibros.html', context)
