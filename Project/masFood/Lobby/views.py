from django.shortcuts import render

# Create your views here.

def lobby_views(request):
    return render(request, 'Lobby\Index.html', context=None)
