from django.db import models

# Create your models here.

class Alimentos(models.Model):
    titulo = models.CharField('Titulo',max_length=20)
    descripción = models.CharField('Descripcion',max_length=200)
    categoria = models.CharField('Categoria',max_length=50)
    imagen = models.CharField('imagen',max_length=100, null=True)

class Recetas(models.Model):
    titulo = models.CharField('Titulo', max_length=20)
    descripción = models.CharField('Descripcion', max_length=200)
    ingredientes = models.CharField('Ingredientes', max_length=300)
    preparación = models.CharField('Preparación', max_length=400)
    imagen = models.CharField('imagen', max_length=100, null=True)

class Comentarios(models.Model):
    user = models.CharField('User', max_length=20)
    coment = models.CharField('Comentario', max_length=300)

class Dietas(models.Model):
    titulo = models.CharField('Titulo', max_length=20)
    descripción = models.CharField('Descripción', max_length=300)
    links = models.CharField('links', max_length=200, null=True)
    imagen = models.CharField('imagen', max_length=100, null=True)



