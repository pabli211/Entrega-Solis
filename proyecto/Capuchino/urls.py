from django.urls import path
from Capuchino.views import *

urlpatterns = [
    path('recetas/', receta, name='receta'),
    path('cheffs/', cheff, name='cheff'),
    path('clientes/', cliente, name='cliente'),
    path('restaurants/', restaurant, name='restaurant'),
    path('inicio/', inicio, name='inicio'),

    path('busquedareceta/', buscarReceta, name='buscarReceta'),
    path('busqueda-receta/', busquedaReceta, name='buscar_receta'),

    path('busquedarest/', buscarRest, name='buscarRest'),
    path('busqueda-restaurant/', busquedaRest, name='buscar_rest'),

    path('busquedachef/', buscarChef, name='buscarChef'),
    path('busqueda-chef/', busquedaChef, name='buscar_chef'),

    path('busquedacliente/', buscarCliente, name='buscarCliente'),
    path('busqueda-cliente/', busquedaCliente, name='buscar_cliente'),
]
