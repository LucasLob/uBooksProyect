from django.db import models
from django.contrib.auth.forms import User
# Create your models here.
from django.db.models import CASCADE
from django.db.models.signals import post_save


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.nombre,self.apellido)


class Editora(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    aniolanzamiento = models.CharField(max_length=4)
    paginas = models.PositiveIntegerField()
    sinopsis = models.TextField(blank=True)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora_id = models.ForeignKey(Editora, null=True, on_delete=models.CASCADE, related_name='editora_id')
    has_categorias = models.ManyToManyField(Categoria)
    imagen = models.URLField(null=True)
    unidades = models.PositiveIntegerField(default="0")
    veces_vendido = models.PositiveIntegerField(default="0")
    momento_creacion = models.DateTimeField(auto_now_add=True)
    momento_modificacion = models.DateTimeField(auto_now=True)
    precio = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return self.titulo
