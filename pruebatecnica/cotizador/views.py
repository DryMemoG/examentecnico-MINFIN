from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
# Create your views here.

#Login
def index(request):
    return render('Hola xd')

#region Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = "Cliente/Clientes.html"

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "Cliente/ClientesDetalle.html"

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Cliente/ClienteForm.html"
    success_url = reverse_lazy("ClienteList")

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Cliente/ClienteForm.html"
    success_url = reverse_lazy("ClienteList")

class ClienteDeleteView(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Cliente/ClienteDeleteForm.html"
    success_url = reverse_lazy("ClienteList")
#endregion

#region Vehiculo
class VehiculoListView(ListView):
    model = Vehiculo
    template_name = "Vehiculo/Vehiculos.html"

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = "Vehiculo/VehiculosDetalle.html"

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "Vehiculo/VehiculoForm.html"
    success_url = reverse_lazy("VehiculoList")

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "Vehiculo/VehiculoForm.html"
    success_url = reverse_lazy("VehiculoList")

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "Vehiculo/VehiculoDeleteForm.html"
    success_url = reverse_lazy("VehiculoList")
#endregion

#region Cotizaciones
class CotizacionListView(ListView):
    model = Cotizacion
    template_name = "Cotizacion/Cotizaciones.html"

class CotizacionDetailView(DetailView):
    model = Cotizacion
    template_name = "Cotizacion/CotizacionesDetalle.html"

class CotizacionCreateView(CreateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = "Cotizacion/CotizacionForm.html"
    success_url = reverse_lazy("CotizacionList")

#endregion



