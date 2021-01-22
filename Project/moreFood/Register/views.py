from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

#Vista de registro
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():#Comprobacion de datos
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)#Lo loguea automaticamente
            return redirect('/')
    else:
        form = UserCreationForm()
    #Renderizamos la template
    return render(request, 'registration\Register.html', {'form': form})
