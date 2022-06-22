
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField (max_length= 150) 

    def __str__(self):
        return self.name

class post (models.Model):
    category = models.ForeignKey (Category, on_delete=models.PROTECT, default=1)
    Titulo = models.CharField(max_length=100)
    Subttítulo = models.CharField(max_length=100)
    Contenido = models.TextField ()
    Autorx = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_post')
    Fecha = models.DateField (default = timezone.now)

def __str__(self):
    return self.Titulo


class Comentarios (models.Model):
    post = models.ForeignKey (User, on_delete=models.CASCADE, related_name='comentarios')
    Nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length = 60) 
    Contenido = models.TextField ()

class Investigadorxs (models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Titulo = models.CharField(max_length=50)
    Pertenencia_institucional = models.CharField(max_length=50)
    Edad = models.IntegerField()
    email = models.EmailField(max_length = 60) 
    
class Publicaciones (models.Model):
    Título = models.CharField(max_length=100)
    Autorxs = models.CharField(max_length=50)
    Pertenencia_institucional_de_autorxs = models.CharField(max_length=50)
    url_de_la_publicacion = models.URLField(max_length = 200)

class Actividades_eventos (models.Model):
    nombre_de_evento = models.CharField(max_length=50)
    Fecha = models.DateTimeField()
    Convoca = models.CharField(max_length=50)
    Participan = models.IntegerField()
    Institucion = models.CharField(max_length=50)
    
class sobre_mi (models.Model):
    acerca_de_mí= models.TextField (max_length= 500)