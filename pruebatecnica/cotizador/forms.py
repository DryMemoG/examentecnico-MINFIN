from django import forms    
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("NIT", "nombres", "apellidos", "email", "telefono", "direccion")

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ("marca", "modelo", "linea", "descripcion","precio")

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ("NIT", "idAuto")
