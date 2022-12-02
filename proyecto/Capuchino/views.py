from django.shortcuts import render
from .models import *
from Capuchino.forms import *



def inicio(request):
    return render(request, 'Capuchino/inicio.html')

def editarBase(request):
    return render(request, 'Capuchino/editarBase.html')



#------------------------Bloque Recetas

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

def buscarReceta(request):
    return render(request, 'Capuchino/buscarReceta.html')

def busquedaReceta(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        receta= Receta.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoReceta.html', {'recetas':receta})

    else:
        return render(request, 'Capuchino/buscarReceta.html', {'mensaje_2':'por favor ingrese una receta'})

def leerReceta(request):
    receta= Receta.objects.all()
    return render(request, 'Capuchino/leerReceta.html', {'recetas':receta})

def eliminarReceta(request, id):
    receta= Receta.objects.get(id=id)
    receta.delete()

    receta= Receta.objects.all()
    return render(request, 'Capuchino/leerReceta.html', {'mensaje':'Receta eliminado correctamente', 'recetas':receta})

def editarReceta(request, id):
    receta= Receta.objects.get(id=id)
    if request.method=='POST':
        form= RecetaForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            receta.nombre= informacion['nombre']
            receta.dificultad= informacion['dificultad']
            receta.pasos= informacion['pasos']
            receta.save()
            receta= Receta.objects.all()
            return render(request, 'Capuchino/leerReceta.html', {'mensaje':'Receta editada correctamente', 'recetas':receta})
            
    else:
        formulario= RecetaForm(initial={'nombre':receta.nombre , 'dificultad':receta.dificultad, 'pasos':receta.pasos})
    return render(request, 'Capuchino/editarReceta.html', {'form':formulario, 'recetas':receta})

#------------------------Bloque Cheff

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
            return render(request,'Capuchino/inicio.html', {'mensaje':'Chef creado correctamente'})
    else:
        formulario= CheffForm()
    
    return render(request, 'Capuchino/cheffs.html', {"form":formulario},)

def buscarChef(request):
    return render(request, 'Capuchino/buscarChef.html')

def busquedaChef(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        chefs= Cheff.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoChef.html', {'chefs':chefs})

    else:
        return render(request, 'Capuchino/buscarChef.html', {'mensaje_2':'por favor ingrese un Chef'})

def leerChef(request):
    chef= Cheff.objects.all()
    return render(request, 'Capuchino/leerChef.html', {'chefs':chef})

def eliminarChef(request, id):
    chef= Cheff.objects.get(id=id)
    chef.delete()

    chef= Cheff.objects.all()
    return render(request, 'Capuchino/leerChef.html', {'mensaje':'Chef eliminado correctamente', 'chefs':chef})

def editarChef(request, id):
    chef= Cheff.objects.get(id=id)
    if request.method=='POST':
        form= CheffForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            chef.nombre= informacion['nombre']
            chef.apellido= informacion['apellido']
            chef.email= informacion['email']
            chef.restaurant= informacion['restaurant']
            chef.especialidad= informacion['especialidad']

            chef.save()
            chef= Cheff.objects.all()
            return render(request, 'Capuchino/leerChef.html', {'mensaje':'Chef editado correctamente', 'chefs':chef})
            
    else:
        formulario= CheffForm(initial={'nombre':chef.nombre , 'apellido':chef.apellido, 'email':chef.email, 'restaurant':chef.restaurant, 'especialidad':chef.especialidad})
    return render(request, 'Capuchino/editarChef.html', {'form':formulario, 'chefs':chef})

#------------------------Bloque Restaurats

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

def buscarRest(request):
    return render(request, 'Capuchino/buscarRest.html')

def busquedaRest(request):

    if request.GET["pepito"]:

        nombre= request.GET["pepito"]
        rest= Restaurant.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoRest.html', {'rest':rest})

    else:
        return render(request, 'Capuchino/buscarRest.html', {'mensaje_2':'por favor ingrese un restaurant'})

def leerRest(request):
    rest= Restaurant.objects.all()
    return render(request, 'Capuchino/leerRest.html', {'rests':rest})

def eliminarRest(request, id):
    rest= Restaurant.objects.get(id=id)
    rest.delete()

    rest= Restaurant.objects.all()
    return render(request, 'Capuchino/leerRest.html', {'mensaje':'Restaurant eliminado correctamente', 'rests':rest})

def editarRest(request, id):
    rest= Restaurant.objects.get(id=id)
    if request.method=='POST':
        form= RestaurantForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            rest.nombre= informacion['nombre']
            rest.direccion= informacion['direccion']
            rest.estrellas= informacion['estrellas']           
            rest.save()
            rest= Restaurant.objects.all()
            return render(request, 'Capuchino/leerRest.html', {'mensaje':'Restaurant editado correctamente', 'rests':rest})
            
    else:
        formulario= RestaurantForm(initial={'nombre':rest.nombre , 'direccion':rest.direccion, 'estrellas':rest.estrellas})
    return render(request, 'Capuchino/editarRest.html', {'form':formulario, 'rests':rest})

#------------------------Bloque Clientes

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

def buscarCliente(request):
    return render(request, 'Capuchino/buscarCliente.html')

def busquedaCliente(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        cliente= Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoCliente.html', {'clientes':cliente})

    else:
        return render(request, 'Capuchino/buscarCliente.html', {'mensaje_2':'por favor ingrese un usuario'})

def leerCliente(request):
    cliente= Cliente.objects.all()
    return render(request, 'Capuchino/leerCliente.html', {'clientes':cliente})

def eliminarCliente(request, id):
    cliente= Cliente.objects.get(id=id)
    cliente.delete()

    cliente= Cliente.objects.all()
    return render(request, 'Capuchino/leerCliente.html', {'mensaje':'Cliente eliminado correctamente', 'clientes':cliente})

def editarCliente(request, id):
    cliente= Cliente.objects.get(id=id)
    if request.method=='POST':
        form= ClienteForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            cliente.nombre= informacion['nombre']
            cliente.apellido= informacion['apellido']
            cliente.email= informacion['email']
            cliente.reseña= informacion['reseña']     
            cliente.save()
            cliente= Cliente.objects.all()
            return render(request, 'Capuchino/leerCliente.html', {'mensaje':'Cliente editado correctamente', 'clientes':cliente})
            
    else:
        formulario= ClienteForm(initial={'nombre':cliente.nombre , 'apellido':cliente.apellido, 'email':cliente.email, 'reseña':cliente.reseña})
    return render(request, 'Capuchino/editarCliente.html', {'form':formulario, 'clientes':cliente})



