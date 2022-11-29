from django.urls import path
from Capuchino.views import *

urlpatterns = [
    path('recetas/', receta, name='receta'),
    path('cheffs/', cheff, name='cheff'),
    path('clientes/', cliente, name='cliente'),
    path('restaurants/', restaurant, name='restaurant'),
    path('inicio/', inicio, name='inicio'),
]
