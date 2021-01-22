from django.conf.urls import url, include
from . import views

#Rutas del aplicativo Lobby
urlpatterns = [
    url(r'^$', views.lobby_views , name='LobbyViews'),
]