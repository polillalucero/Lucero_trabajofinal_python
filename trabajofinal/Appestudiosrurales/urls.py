from django.urls import path
from Appestudiosrurales.views import categorias, posts, comentarios, actividades_eventos, investigadorxs, publicaciones_home, about_me
from Appestudiosrurales.views import mi_home 

 
urlpatterns = [
path ('categorias/', categorias),
path ('posts/', posts),
path ('comentarios/', comentarios),
path ('actividades_eventos/', actividades_eventos),
path ('investigadorxs/', investigadorxs),
path ('publicaciones_home/', publicaciones_home),
path ('about_me/', about_me), 
path ('mi_home/', mi_home),
]