from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
import requests
from .forms import RegistroUsuarioForm, InicioSesionForm


POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon/'

#Vista página principal
def pagina_principal(request):
    respuesta = requests.get(POKEAPI_URL)
    informacion = respuesta.json()
    resultados = informacion.get('results', [])
    contexto = {
        'resultados': resultados,
    }
    return render(request, 'index.html', contexto)



#Vista para visualizar Pokemon
@login_required  
def visualizar_pokemon(request, pokemon_name):
    respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
    if respuesta.status_code == 200:
        info_pokemon = respuesta.json()
        contexto = {
            'pokemon': info_pokemon, 
        }
        return render(request, 'visualizar_pokemon.html', contexto)
    else:
        error_mensaje = f"No se pudo encontrar información para el Pokémon {pokemon_name}."
        contexto = {
            'error_message': error_mensaje,
        }
        return render(request, 'visualizar_pokemon.html', contexto)

#Vista Registro de usuario
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('inicio_sesion')
    else:
        form = RegistroUsuarioForm()
    contexto = {'form': form}
    return render(request, 'registration/registrar.html', contexto)

#Vista inicio de sesion
def inicio_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pagina_principal')
    else:
        form = InicioSesionForm()
    contexto = {
        'form': form,
    }
    return render(request, 'registration/login.html', contexto)

#Vista cerrar sesion
def cerrar_sesion(request):
    logout(request)
    return redirect('pagina_principal')
