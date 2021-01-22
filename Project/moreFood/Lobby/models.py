from django.db import models

# Create your models here.

#Tabla de Alimentos
class Alimentos(models.Model):
    #Campo titulo
    titulo = models.CharField('Titulo',max_length=20)
    # Campo descripcion
    descripción = models.CharField('Descripcion',max_length=200)
    # Campo categoria
    categoria = models.CharField('Categoria',max_length=50)
    # Campo imagen
    imagen = models.CharField('imagen',max_length=100, null=True)

#Tabla de Recetas
class Recetas(models.Model):
    # Campo titulo
    titulo = models.CharField('Titulo', max_length=20)
    # Campo descripcion
    descripción = models.CharField('Descripcion', max_length=200)
    # Campo ingredientes
    ingredientes = models.CharField('Ingredientes', max_length=300)
    # Campo preparación
    preparación = models.CharField('Preparación', max_length=400)
    # Campo imagen
    imagen = models.CharField('imagen', max_length=100, null=True)

#Esta tabla no la hemos usado
class Comentarios(models.Model):
    user = models.CharField('User', max_length=20)
    coment = models.CharField('Comentario', max_length=300)

#Tabla de Dietas
class Dietas(models.Model):
    # Campo titulo
    titulo = models.CharField('Titulo', max_length=20)
    # Campo descripcion
    descripción = models.CharField('Descripción', max_length=300)
    # Campo links
    links = models.CharField('links', max_length=200, null=True)
    # Campo imagen
    imagen = models.CharField('imagen', max_length=100, null=True)



