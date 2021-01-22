from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario que registra el usuario
class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']#Campos del formulario


