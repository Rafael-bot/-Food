from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.shortcuts import render

from .models import Alimentos, Dietas, Recetas


# Create your views here.

def enviar_correo(nombre, apellido, userEmail, tlfn, continente, tema, mensaje):
    # print(nombre,apellido,compañia,userEmail,tlfn,continente,tema,mensaje)

    email = EmailMultiAlternatives(
        tema,
        nombre + ' ' + apellido + ' desea: \n' + mensaje + '.\n A contactado atraves del email ' + userEmail + '.\n Y con telefono ' + tlfn + ' . \n Desde ' + continente,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]
    )

    email.send()


@login_required
def lobby_views(request):
    a = Alimentos.objects.all()
    d = Dietas.objects.all()
    r = Recetas.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')

        userEmail = request.POST.get('userEmail')
        tlfn = request.POST.get('tlfn')
        continente = request.POST.get('continente')
        tema = request.POST.get('tema')
        mensaje = request.POST.get('mensaje')
        enviar_correo(nombre, apellido, userEmail, tlfn, continente, tema, mensaje)

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

    return render(request, 'Index.html', context={'alimentos': a, 'dietas': d, 'recetas': r})

