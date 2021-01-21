from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Alimentos, Dietas


# Create your views here.



@login_required
def lobby_views(request):
    a = Alimentos.objects.order_by('categoria')
    d = Dietas.objects.order_by('titulo')
    return render(request, 'Index.html', context={'alimentos': a, 'dietas':d})


