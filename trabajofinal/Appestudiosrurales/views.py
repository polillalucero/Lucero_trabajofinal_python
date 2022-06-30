
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from Appestudiosrurales.models import Category, post, Comentarios, Investigadorxs, Publicaciones, Actividades_eventos, sobre_mi
from Appestudiosrurales.forms import InvestigadorxsFormulario, PublicacionesFormulario, UserRegistrationForm, UserEditForm
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def mi_home (request):
  home = loader.get_template('Appestudiosrurales/home.html ')
  documento = home.render()
  return HttpResponse (documento)

def categorias (request):
  return HttpResponse ("No hay publicaciones aún")
  return render (request, 'Appestudiosrurales/Categorias.html')

def posts (request):
  return render(request, 'Appestudiosrurales/Posts.html')

def comentarios (request):
  return HttpResponse ("No hay publicaciones aún")
  return render(request, 'Appestudiosrurales/comentarios')

def investigadorxs (request):
  return render(request, 'Appestudiosrurales/investigadorxs.html')

def publicaciones_home (request):
  return render(request, 'Appestudiosrurales/publicaciones_home.html')

def actividades_eventos (request):
  return render(request, 'Appestudiosrurales/ActividadesyEventos.html')

def about_me (request):
 return render(request, 'Appestudiosrurales/sobre mí.html')


def investigadorxsFormulario(request):
  if request.method == 'POST': 
    miFormulario = InvestigadorxsFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    Nombre = informacion['Nombre']
    Apellido = informacion ['Apellido']
    Titulo = informacion ['Titulo']
    Pertenencia_institucional = informacion ['Pertenencia_institucional']
    Edad =informacion ['Edad']
    email =informacion ['email']
    investigadorxs = Investigadorxs (Nombre = Nombre, Apellido = Apellido, Titulo = Titulo, Pertenencia_institucional = Pertenencia_institucional, Edad = Edad, email = email)
    investigadorxs.save()
    return render (request, 'Appestudiosrurales/home.html')
  else :
    miFormulario = InvestigadorxsFormulario()
  return render(request, 'Appestudiosrurales/investigadorxsFormulario.html', {'miFormulario': miFormulario})

def busquedainvestigadorx (request):
   return render (request, 'Appestudiosrurales/busquedaInvestigadorx.html')

def buscar (request):
  if request.GET['Apellido']:
    Apellido = request.GET ["Apellido"]
    investigadorsx = Investigadorxs.objects.filter (Apellido=Apellido) 
    return render (request, 'Appestudiosrurales/resultadosBusqueda.html', {'investigadorxs': investigadorxs, 'Apellido': Apellido})
  else: 
    respuesta = "No se ha ingresado ningún apellido"  
  return HttpResponse (respuesta)

 #CRUD READ
def leerPublicaciones (request):
      publicaciones = Publicaciones.objects.all()
      contexto = {'publicaciones': publicaciones}
      return render (request, 'Appestudiosrurales/publicaciones_home.html', contexto)

# CRUD CREATE

def publicacionesFormulario(request):
  if request.method == 'POST': 
    miFormulario = PublicacionesFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    Título = informacion ['Título']
    Autorxs = informacion ['Autorxs']
    Pertenencia_institucional_de_autorxs = informacion['Pertenencia_institucional_de_autorxs']
    url_de_la_publicacion = informacion ['url_de_la_publicacion' ]
    publicaciones = Publicaciones (Título = Título, Autorxs = Autorxs, Pertenencia_institucional_de_autorxs = Pertenencia_institucional_de_autorxs, url_de_la_publicacion = url_de_la_publicacion )
    publicaciones.save()
    return render (request, 'Appestudiosrurales/home.html')
  else:
      miFormulario = PublicacionesFormulario()
  return render (request, 'Appestudiosrurales/publicacionesFormulario.html', {'miFormulario': miFormulario})

#CRUD DELETE

@login_required
def eliminarPublicacion (request, Título):
    publicacion = Publicaciones.objects.get(Título = Título)
    publicacion.delete()
    publicaciones = Publicaciones.objects.all()
    contexto = {'publicaciones': publicaciones}
    return render (request, 'Appestudiosrurales/publicaciones_home.html', contexto)

@login_required
def editarPublicacion (request, publicaciones_Título):
  publicaciones = Publicaciones.get(publicaciones = publicaciones_Título)
  if request.method  == 'POST':
    miFormulario = publicacionesFormulario(request.POST)
  if miFormulario.is_valid():
     informacion = miFormulario.cleaned_data
     publicaciones.Título = informacion ['Título']
     publicaciones.Autorxs = informacion ['Autorxs']
     publicaciones.Pertenencia_institucional_de_autorxs = informacion['Pertenencia_institucional_de_autorxs']
     publicaciones.url_de_la_publicacion = informacion ['url_de_la_publicacion']
     publicaciones.save()
     publicaciones = Publicaciones.objects.all()
     contexto = {'publicaciones' : publicaciones}
     return render (request, 'Appestudiosrurales/publicaciones_home.html', contexto)
  else: 
     miFormulario = publicacionesFormulario (initial={'Título': publicaciones.Título, 'Autorxs':publicaciones.Autorxs, 'Pertenencia_institucional_de_autorxs' : publicaciones.Pertenencia_institucional_de_autorxs, 'url_de_la_publicacion' : publicaciones.url_de_la_publicacion})
     contexto = {'miFormulario':miFormulario,'publicaciones_Título': publicaciones_Título}
     return render (request, 'Appestudiosrurales/editarPublicacion.html', contexto )


#ListView

class ActividadesyeventosList(LoginRequiredMixin, ListView):
  model = Actividades_eventos
  template_name = 'Appestudiosrurales/actividades_eventos_list.html'

#DetailView
class ActividadesyeventosDetalle (DetailView):
  model = Actividades_eventos
  template_name= 'Appestudiosrurales/actividades_eventos_detalle.html'

class ActividadesyeventosCreacion (CreateView):
  model = Actividades_eventos
  success_url = reverse_lazy ('atividades_eventos_listar')
  fields = ['nombre_de_evento', 'Fecha', 'Convoca', 'Participan', 'Institucion']  

class ActividadesyeventosEdicion(UpdateView):
  model = Actividades_eventos
  success_url = reverse_lazy('actividades_eventos_listar')
  fields = ['nombre_de_evento', 'Fecha', 'Convoca', 'Participan', 'Institucion']  

class ActividadesyeventosEliminacion(DeleteView):
  model = Actividades_eventos
  success_url = reverse_lazy('actividades_eventos_listar')



#--------------------------------------------------------------------
#LOGIN

def login_request(request):
  if request.method == 'POST':
     form = AuthenticationForm(request, request.POST)
     if form.is_valid():
      usuario = form.cleaned_data.get ('username')
      clave = form.cleaned_data.get('password')
      user = authenticate(username= usuario, password =clave) 
      if user is not None: 
        login(request, user)
        return render (request, 'Appestudiosrurales/home.html', {'mensaje': f'Bienvenide {usuario}'})
      else:
       return render (request, 'Appestudiosrurales/home.html', {'mensaje': ' Error,datos incorrectos'})
     else:
      return render (request, 'Appestudiosrurales/home.html', {'mensaje': ' Error formulario erróneo'})
  else:
      form = AuthenticationForm()
      return render(request, 'Appestudiosrurales/login.html', {'form': form})



def register_request (request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return render (request, 'Appestudiosrurales/home.html', {'mensaje': f'Usuario {username}creado correctamente'})
    else:
      return render (request, 'Appestudiosrurales/home.html', {'mensaje': f'Error,No se pudo crear el usuario'})
  else:
      form = UserRegistrationForm()
      return render(request, 'Appestudiosrurales/register.html', {'form': form})

@login_required
def editarPerfil(request):
  usuario = request.user
  if request.method == 'POST':
    formulario = UserEditForm(request.POST, instance=usuario)
    if formulario.is_valid():
      informacion = formulario.cleaned_data
      usuario.email = informacion['email']
      usuario.password1 = informacion['password1']
      usuario.password2 = informacion['password2']
      usuario.save()
      return render(request, 'Appestudiosrurales/home.html', {'mensaje': 'Datos cambiados exitosamente'})
  else:
    formulario = UserEditForm(instance=usuario)
  return render(request,'Appestudiosrurales/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})