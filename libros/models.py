from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    imagen = models.URLField()
    sinopsis = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, blank=True)
    autor = models.CharField(max_length=50, blank=True)
    genero = models.CharField(max_length=50, blank=True)
    editora = models.CharField(max_length=50, blank=True)
    anioLanzamiento = models.CharField(max_length=50)
    paginas = models.IntegerField()
    encuadernacion = models.CharField(max_length=15)

    def __str__(self):
        return self.titulo