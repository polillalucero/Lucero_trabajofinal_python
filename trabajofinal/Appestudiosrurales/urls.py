from django.urls import path
from Appestudiosrurales.views import categorias, posts, comentarios, actividades_eventos, investigadorxs, publicaciones_home, about_me, mi_home, investigadorxsFormulario, publicacionesFormulario,busquedainvestigadorx , buscar, leerPublicaciones, eliminarPublicacion, editarPublicacion, ActividadesyeventosList, ActividadesyeventosDetalle, ActividadesyeventosCreacion, ActividadesyeventosEdicion, ActividadesyeventosEliminacion, login_request, register_request, editarPerfil, postList, postDetalle, investigadorxsList, investigadorxsDetalle
from django.contrib.auth.views import LogoutView
 
urlpatterns = [
path ('categorias/', categorias),
path ('posts/', posts, name = 'Posts'),
path ('comentarios/', comentarios, name= 'Comentarios'),
path ('ActividadesyEventos/', actividades_eventos, name = 'Actividades y Eventos'),
path ('investigadorxs/', investigadorxs, name = 'Investigadorxs'),
path ('about_me/', about_me, name = 'Sobre mí'), 
path ('', mi_home),
path ('investigadorxsFormulario/', investigadorxsFormulario, name = 'investigadorxsFormulario'), 
path ('publicacionesFormulario/', publicacionesFormulario, name= 'publicacionesFormulario'), 
path ('busquedaInvestigadorx/', busquedainvestigadorx, name = 'busquedainvestigadorx'),
path ('resultadosBusqueda/', buscar, name = 'buscar'),
path ('publicaciones_home/', leerPublicaciones, name = 'publicaciones_home'), #ver si el error está acá 
path ('eliminarPublicacion/<Titulo>', eliminarPublicacion, name = 'eliminarPublicacion'),
path ('editarPublicacion/<Titulo>', editarPublicacion, name = 'editarPublicacion'),

path('actividades_eventos/list/', ActividadesyeventosList.as_view(), name = 'actividades_eventos_listar'),
path('actividades_eventos/<pk>', ActividadesyeventosDetalle.as_view(), name = 'actividades_eventos_detalle'),
path('actividades_eventos/nuevo/', ActividadesyeventosCreacion.as_view(), name = 'actividades_eventos_crear'),
path('actividades_eventos/editar/<pk>', ActividadesyeventosEdicion.as_view(), name = 'actividades_eventos_editar'),
path('actividades_eventos/borrar/<pk>', ActividadesyeventosEliminacion.as_view(), name = 'actividades_eventos_borrar'),
path ('investigadorxsList/list/', investigadorxsList.as_view(), name = 'investigadorxsList' ),
path ('investigadorxs_detalle/<pk>', investigadorxsDetalle.as_view(), name = 'investigadorxs_detalle'),
path('postList/list/', postList.as_view(), name = 'postList'), 
path ('Post_detalle/<pk>', postDetalle.as_view(), name = 'Post_detalle'),
path('login/', login_request, name = 'login'),
path ('register/', register_request, name = 'register'),
path ('logout/', LogoutView.as_view(template_name='Appestudiosrurales/logout.html'), name = 'logout'),
path('editarPerfil', editarPerfil, name='editarPerfil'),
]