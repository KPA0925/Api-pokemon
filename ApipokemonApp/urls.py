from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #Vistas de la página principal, visualizar pokemon, registrarse, iniciar sesion y cerrar sesion
    path('', views.pagina_principal, name='pagina_principal'),
    path('pokemon/<str:pokemon_name>/', views.visualizar_pokemon, name='visualizar_pokemon'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('iniciar-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
