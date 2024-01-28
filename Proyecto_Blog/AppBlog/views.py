from django.shortcuts import render
from AppBlog.models import *
from AppBlog.forms import *
from django.http import request
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def inicio(request):
    
    return render(request, "Principal.html")

def About(request):
    return render(request, "About.html")

#APARTADO DE MANGAS

def manga(request):
    
    mis_mangas = Manga.objects.all()
    
    info = {"mangas":mis_mangas}
    
    return render(request, "Manga.html", info)

@login_required(login_url='/login_bloqueo/')
def manganuevo(request):
    
    if request.method == "POST":
        
        nuevo_formulario = MangaForm(request.POST)
        
        if nuevo_formulario.is_valid():
            
            info = nuevo_formulario.cleaned_data
            
            manga_nuevo = Manga(TituloManga=info["Titulo"], 
                                GeneroManga=info["Genero"], 
                                BreveExp=info["Sintaxis"], 
                                )
            
            manga_nuevo.save()
            return render(request, "Principal.html")
    else:
        nuevo_formulario = MangaForm()
        
    return render(request, "manganuevo.html", {"Mi_formu":nuevo_formulario})

@login_required(login_url='/login_bloqueo/')
def actualizarmanga(request, nombre_manga):
    
    manga_elegido = Manga.objects.get(TituloManga= nombre_manga)
    
    if request.method == "POST":
        
        registro_nuevo = MangaForm(request.POST)
        
        if registro_nuevo.is_valid():
            
            info = registro_nuevo.cleaned_data
            
            manga_elegido.TituloManga = info["Titulo"]
            manga_elegido.GeneroManga = info["Genero"]
            manga_elegido.BreveExp = info["Sintaxis"]
            
            manga_elegido.save()
            
            return render(request, "Principal.html")
    else:
        registro_nuevo = MangaForm(initial={"Titulo":manga_elegido.TituloManga, 
                                            "Genero":manga_elegido.GeneroManga, 
                                            "Sintaxis":manga_elegido.BreveExp}
                                   )
        
    return render(request, "actualizarmanga.html", {"mi_formu":registro_nuevo})

@login_required(login_url='/login_bloqueo/')
def borrarmanga(request, nombre_manga):
    
    manga_elegido = Manga.objects.get(TituloManga= nombre_manga)
    
    manga_elegido.delete()
    
    return render(request, "Principal.html")

# APARTADO DE JUEGOS 

def games(request):
    
    mis_juegos = Games.objects.all()
    
    info = {"games":mis_juegos}
    
    return render(request, "games.html", info)

@login_required(login_url='/login_bloqueo/')
def gamesnuevo(request):
    
    if request.method == "POST":
        
        nuevo_formulario = GamesForm(request.POST)
        
        if nuevo_formulario.is_valid():
            
            info = nuevo_formulario.cleaned_data
            
            game_nuevo = Games(TituloGame=info["Titulo"], 
                                GeneroGame=info["Genero"], 
                                BreveExp=info["Sintaxis"], 
                                )
            
            game_nuevo.save()
            return render(request, "Principal.html")
    else:
        nuevo_formulario = GamesForm()
        
    return render(request, "nuevogames.html", {"Mi_formu":nuevo_formulario})

@login_required(login_url='/login_bloqueo/')
def actualizargames(request, nombre_juego):
    
    juego_elegido = Games.objects.get(TituloGame= nombre_juego)
    
    if request.method == "POST":
        
        registro_nuevo = GamesForm(request.POST)
        
        if registro_nuevo.is_valid():
            
            info = registro_nuevo.cleaned_data
            
            juego_elegido.TituloGame = info["Titulo"]
            juego_elegido.GeneroGame = info["Genero"]
            juego_elegido.BreveExp = info["Sintaxis"]
            
            juego_elegido.save()
            
            return render(request, "Principal.html")
    else:
        registro_nuevo = GamesForm(initial={"Titulo":juego_elegido.TituloGame, 
                                            "Genero":juego_elegido.GeneroGame, 
                                            "Sintaxis":juego_elegido.BreveExp}
                                   )
        
    return render(request, "actualizargame.html", {"mi_formu":registro_nuevo})

@login_required(login_url='/login_bloqueo/')
def borrargames(request, nombre_juego):
    
    juego_elegido = Games.objects.get(TituloGame= nombre_juego)
    
    juego_elegido.delete()
    
    return render(request, "Principal.html")


#APARTADO DE PERFILES

def inicio_sesion(request):
    
        if request.method == 'POST':
        
            formulario = AuthenticationForm(request, data = request.POST)
        
            if formulario.is_valid():
            
                usuario = formulario.cleaned_data.get('username')
                contra = formulario.cleaned_data.get('password')
            
                user = authenticate(username=usuario, password=contra)
            
                if user is not None:
                   login(request, user)
                   return render(request, "Principal.html", {"mensaje":f"Bienvenido !{usuario}!"})
            else:
                return render(request, "Principal.html", {"mensaje":f"Error, Datos incorrectos"} )
            
        else:
            formulario = AuthenticationForm()
            
        return render(request, "registro/login.html", {"formu":formulario})
    
def inicio_sesion_bloqueo(request):
    
        if request.method == 'POST':
        
            formulario = AuthenticationForm(request, data = request.POST)
        
            if formulario.is_valid():
            
                usuario = formulario.cleaned_data.get('username')
                contra = formulario.cleaned_data.get('password')
            
                user = authenticate(username=usuario, password=contra)
            
                if user is not None:
                   login(request, user)
                   return render(request, "Principal.html", {"mensaje":f"Bienvenido !{usuario}!"})
            else:
                return render(request, "Principal.html", {"mensaje":f"Error, Datos incorrectos"} )
            
        else:
            formulario = AuthenticationForm()
            
        return render(request, "registro/login_bloqueo.html", {"formu":formulario})
    
def registro(request):
    
    if request.method == "POST":
        
        formulario = CustomUserCreationForm(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = info['username']
            formulario.save()
            return render(request, "Principal.html", {"mensaje":f"Bienvenido !{usuario}!"})
        
    formulario = CustomUserCreationForm()
    return render(request, "registro/sign_up.html", {"formu":formulario})
        
    
def cerrar_sesion(request):
    logout(request)
    return render(request, 'registro/cerrar_sesion.html')

def editar_perfil(request):
    
    usuario_elegido = request.user
    
    if request.method == "POST":
        
        formulario = EditarUsuario(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario_elegido.username = info["username"]
            usuario_elegido.email = info["email"]
            usuario_elegido.set_password(info["password1"])
            
            usuario_elegido.save()
            return render(request, "Principal.html", {"mensaje":f"Bienvenido !{usuario_elegido}!"})
        
    formulario = EditarUsuario(initial={'username':usuario_elegido.username, 'email':usuario_elegido.email, 'password':usuario_elegido.password })
     
    return render(request, "registro/editar_perfil.html", {"formu":formulario})

def view_perfil(request):
    
    return render(request, "registro/Perfil.html")
            
        