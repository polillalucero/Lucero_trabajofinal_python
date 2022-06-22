
from django.http import HttpResponse
from django.shortcuts import render
from Appestudiosrurales.models import Category, post, Comentarios, Investigadorxs, Publicaciones, Actividades_eventos, sobre_mi
from django.template import loader


def categorias (self):
    categorias = Category (name = 'género_y_ruralidad')
    categorias.save()
    documento = f"Category: {categorias.name}"
    return HttpResponse (documento)
# Create your views here.

def posts (self):
  documento = f"Página de posts"
  return HttpResponse(documento)

def comentarios (self):
  documento = f"Página de comentarios"
  return HttpResponse(documento)

def investigadorxs (self):
  documento = f"Página de investigadorxs"
  return HttpResponse(documento)

def publicaciones_home (self):
  documento = f"Página de publicaciones"
  return HttpResponse(documento)

def actividades_eventos (self):
  documento = f"Página de Actividades y Eventos"
  return HttpResponse(documento)

def about_me (self):
  documento = f"Sobre mí"
  return HttpResponse(documento)

def mi_home (self):
  home = loader.get_template('home.html')
  documento = home.render() 
  return HttpResponse (documento)



