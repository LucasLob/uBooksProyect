from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from usuarios.forms import FormRegistro, FormEditar, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == "POST":
        form = FormRegistro(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'books/index.html')

    else:
        form = FormRegistro()
        context = {'form': form}
        return render(request, 'usuarios/registro.html', context)


def login_usuario(request):
    form = LoginForm()
    mensajes_error = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                mensajes_error.append('Correo de usuario o la contraseña son incorrectos.')
            else:
                if user.is_active:
                    login(request, user)
                    return redirect(request.GET.get('next', 'inicio'))
                else:
                    mensajes_error.append('El usuario no está activo.')
    else:
        form = LoginForm()
    context = {
        'errores': mensajes_error,
        'login_form': form
    }
    return render(request, 'usuarios/login.html', context)

@login_required
def logout_usuario(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('inicio')

@login_required
def perfil(request):
    context = {
        'user': request.user
    }
    return render(request, 'usuarios/perfil.html', context)

@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = FormEditar(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = FormEditar(instance=request.user)
        context = {'formulario': form}
        return render(request, 'usuarios/perfil_edit.html', context)

def cambio_contrasenia(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('perfil')
        else:
            return redirect('cambiocontrasenia')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'formulario': form}
        return render(request, 'usuarios/cambio_contrasenia.html', context)

