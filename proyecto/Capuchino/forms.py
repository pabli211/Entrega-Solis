from django import forms


class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    reseña= forms.CharField(max_length=2500)

class RecetaForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    dificultad= forms.CharField(max_length=50)
    pasos= forms.CharField(max_length=2500)

class CheffForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()
    restaurant= forms.CharField(max_length=30)
    especialidad= forms.CharField(max_length=50)

class RestaurantForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    direccion= forms.CharField(max_length=30)
    estrellas= forms.IntegerField()