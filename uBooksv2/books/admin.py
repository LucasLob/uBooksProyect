from django.contrib import admin
from books.models import Libro, Autor, Editora, Categoria

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Categoria)