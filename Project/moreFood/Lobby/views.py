from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def lobby_views(request):
    return render(request, 'Index.html', context=None)


