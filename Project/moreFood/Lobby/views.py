from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Alimentos

# Create your views here.



@login_required
def lobby_views(request):
    a = Alimentos.objects.order_by('categoria')
    return render(request, 'Index.html', context={'alimentos': a})


