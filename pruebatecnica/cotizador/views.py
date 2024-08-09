from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

#Login
@login_required
def index(request):
    return render(request, 'main.html')

def custom_logout(request):
    logout(request)
    # Redirige a la página que desees después de cerrar sesión
    return redirect('MainPage')
#region Cliente

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "Cliente/Clientes.html"


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "Cliente/ClientesDetalle.html"

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Cliente/ClienteForm.html"
    success_url = reverse_lazy("ClienteList")

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "Cliente/ClienteFormEdit.html"
    success_url = reverse_lazy("ClienteList")


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "Cliente/ClienteDeleteForm.html"
    success_url = reverse_lazy("ClienteList")
#endregion

#region Vehiculo

class VehiculoListView(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = "Vehiculo/Vehiculos.html"


class VehiculoDetailView(LoginRequiredMixin, DetailView):
    model = Vehiculo
    template_name = "Vehiculo/VehiculosDetalle.html"

class VehiculoCreateView(LoginRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "Vehiculo/VehiculoForm.html"
    success_url = reverse_lazy("VehiculoList")


class VehiculoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "Vehiculo/VehiculoFormEdit.html"
    success_url = reverse_lazy("VehiculoList")


class VehiculoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    template_name = "Vehiculo/VehiculoDeleteForm.html"
    success_url = reverse_lazy("VehiculoList")
#endregion

#region Cotizaciones

class CotizacionListView(LoginRequiredMixin, ListView):
    model = Cotizacion
    template_name = "Cotizacion/Cotizaciones.html"


class CotizacionDetailView(LoginRequiredMixin, DetailView):
    model = Cotizacion
    template_name = "Cotizacion/CotizacionesDetalle.html"


class CotizacionCreateView(LoginRequiredMixin, CreateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = "Cotizacion/CotizacionForm.html"
    success_url = reverse_lazy("CotizacionList")

#endregion



