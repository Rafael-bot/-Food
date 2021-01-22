from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.shortcuts import render

from .models import Alimentos, Dietas, Recetas


# Create your views here.

#Funcion de enviar correo
def enviar_correo(nombre, apellido, userEmail, tlfn, continente, tema, mensaje):

    #Preparamos el correo
    email = EmailMultiAlternatives(
        tema,
        nombre + ' ' + apellido + ' desea: \n' + mensaje + '.\n A contactado atraves del email ' + userEmail + '.\n Y con telefono ' + tlfn + ' . \n Desde ' + continente,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]
    )
    #Enviamos el email
    email.send()

#Para aplicarse esta funcion se necesita estar logueado
@login_required
def lobby_views(request):
    #Almacenamos en objetos los datos cada tabla
    a = Alimentos.objects.all()
    d = Dietas.objects.all()
    r = Recetas.objects.all()

    #--------------------------------Email
    if request.method == 'POST':
        #Preparamos los campos
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        userEmail = request.POST.get('userEmail')
        tlfn = request.POST.get('tlfn')
        continente = request.POST.get('continente')
        tema = request.POST.get('tema')
        mensaje = request.POST.get('mensaje')
        #Llamamo a la funcion enviar_correo
        enviar_correo(nombre, apellido, userEmail, tlfn, continente, tema, mensaje)


    #----------------------------------------------------------Busquedas
    busquedaDieta = request.GET.get("buscarDieta")
    if busquedaDieta:
        d = Dietas.objects.filter(
            Q(titulo__icontains=busquedaDieta)
        ).distinct()

    busquedaReceta = request.GET.get("buscarReceta")
    if busquedaReceta:
        r = Recetas.objects.filter(
            Q(titulo__icontains=busquedaReceta)
        ).distinct()


    busquedaAlimento = request.GET.get("buscarAlimentos")
    if busquedaAlimento:
        a = Alimentos.objects.filter(
            Q(titulo__icontains=busquedaAlimento)|
            Q(categoria__icontains=busquedaAlimento)
        ).distinct()



    return render(request, 'Index.html', context={'alimentos': a, 'dietas': d, 'recetas': r})

