
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

def posts (request):
  return render(request, 'Appestudiosrurales/Posts.html')


def comentarios (request):
  return render(request, 'Appestudiosrurales/comentarios')

def investigadorxs (request):
  return render(request, 'Appestudiosrurales/investigadorxs.html')

def publicaciones_home (request):
 return render(request, 'Appestudiosrurales/Publicaciones.html')

def actividades_eventos (request):
  return render(request, 'Appestudiosrurales/Actividades y Eventos.html')

def about_me (request):
 return render(request, 'Appestudiosrurales/sobre mí.html')

def mi_home (request):
  home = loader.get_template('Appestudiosrurales/home.html ')
  documento = home.render()
  return HttpResponse (documento)



