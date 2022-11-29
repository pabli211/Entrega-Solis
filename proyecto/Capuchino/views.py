from django.shortcuts import render
from .models import *
from Capuchino.forms import *


def inicio(request):
    return render(request, 'Capuchino/inicio.html')

def cliente(request):
    if request.method == "POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            email= informacion['email']
            reseña= informacion['reseña']

            cliente= Cliente(nombre=nombre, apellido=apellido, email=email, reseña=reseña)
            cliente.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Éxito al enviar la reseña'})
    else:
        formulario= ClienteForm()
    
    return render(request, 'Capuchino/clientes.html', {"form":formulario},)

def cheff(request):
    if request.method == "POST":
        form= CheffForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            email= informacion['email']
            restaurant= informacion['restaurant']
            especialidad= informacion['especialidad']

            cheff= Cheff(nombre=nombre, apellido=apellido, email=email, restaurant=restaurant, especialidad=especialidad)
            cheff.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Cheff creado correctamente'})
    else:
        formulario= CheffForm()
    
    return render(request, 'Capuchino/cheffs.html', {"form":formulario},)

def restaurant(request):
    if request.method == "POST":
        form= RestaurantForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            direccion= informacion['direccion']
            estrellas= informacion['estrellas']

            restaurant= Restaurant(nombre=nombre, direccion=direccion, estrellas=estrellas)
            restaurant.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Restaurant añadido correctamente'})
    else:
        formulario= RestaurantForm()
    
    return render(request, 'Capuchino/restaurants.html', {"form":formulario},)

def receta(request):
    if request.method == "POST":
        form= RecetaForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            dificultad=informacion['dificultad']
            pasos=informacion['pasos']

            receta= Receta(nombre=nombre, dificultad=dificultad, pasos=pasos)
            receta.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Receta guardada correctamente'})
    else:
        formulario= RecetaForm()
    
    return render(request, 'Capuchino/recetas.html', {"form":formulario},)

