from django.conf.urls import url, include
from . import views

#Rutas del aplicativo register
urlpatterns = [
    url(r'^$', views.register , name='RegisterViews'),
]