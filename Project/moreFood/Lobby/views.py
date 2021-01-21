from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import render, redirect

from django.conf import settings
from .models import Alimentos, Dietas, Recetas
from django.core.mail import EmailMultiAlternatives



# Create your views here.

def enviar_correo(nombre,apellido,userEmail,tlfn,continente,tema,mensaje):
    #print(nombre,apellido,compañia,userEmail,tlfn,continente,tema,mensaje)

    email = EmailMultiAlternatives(
        tema,
        nombre+' '+apellido+' desea: \n'+mensaje+'.\n A contactado atraves del email '+userEmail+'.\n Y con telefono '+tlfn+' . \n Desde '+continente,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]
    )

    email.send()

@login_required
def lobby_views(request):

    if request.method == 'POST':
        nombre =  request.POST.get('nombre')
        apellido =  request.POST.get('apellido')

        userEmail =  request.POST.get('userEmail')
        tlfn =  request.POST.get('tlfn')
        continente =  request.POST.get('continente')
        tema =  request.POST.get('tema')
        mensaje =  request.POST.get('mensaje')
        enviar_correo(nombre,apellido,userEmail,tlfn,continente,tema,mensaje)

    a = Alimentos.objects.order_by('categoria')
    d = Dietas.objects.order_by('titulo')
    r = Recetas.objects.order_by('titulo')
    return render(request, 'Index.html', context={'alimentos': a, 'dietas':d, 'recetas': r})


