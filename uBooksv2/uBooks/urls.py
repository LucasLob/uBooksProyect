from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from books.views import home, detalle, crear_libro, listado_libros
from usuarios.views import (
    registro,
    perfil,
    login_usuario,
    logout_usuario,
    editar_perfil,
    cambio_contrasenia,
    )
from django.contrib.auth.views import password_reset, \
    password_reset_done, \
    password_reset_confirm, \
    password_reset_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    # Libros
    path('', home, name='inicio'),
    re_path(r'^libro/(?P<pk>[0-9]+)/$', detalle, name='detalle'),
    path('libros/', listado_libros, name="listadolibros"),
    path('libro/nuevo', crear_libro, name="crearlibro"),

    # Usuarios
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar', editar_perfil, name='editar'),
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
    path('perfil/cambio-contrasenia', cambio_contrasenia, name="cambiocontrasenia"),
    path('reinicio-contrasenia/', password_reset, name="reiniciocontrasenia"),
    path('reinicio-contrasenia/ir/', password_reset_done, name="password_reset_done"),
    url(r'^reinicio-contrasenia/confirmacion/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),
    path('reinicio-contrasenia/listo/', password_reset_complete, name="password_reset_complete"),


]
