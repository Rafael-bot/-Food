from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.lobby_views , name='LobbyViews'),
]