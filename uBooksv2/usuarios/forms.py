from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    usr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-xs-3'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-xs-3'}))


class FormRegistro(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-xs-3'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-xs-3'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-xs-3'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control col-xs-3'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control col-xs-3'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control col-xs-3'}))

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(FormRegistro, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class FormEditar(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )