from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="MainPage"),
    #cliente
    path('cliente/', ClienteListView.as_view(), name="ClienteList"),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name="ClienteDetail"),
    path('cliente/new/', ClienteCreateView.as_view(), name="ClienteNew"),
    path('cliente/<int:pk>/edit/', ClienteUpdateView.as_view(), name="ClienteEdit"),
    path('cliente/<int:pk>/delete/', ClienteDeleteView.as_view(), name="ClienteDelete"),
    #Vehiculo
    path('vehiculo/', VehiculoListView.as_view(), name="VehiculoList"),
    path('vehiculo/<int:pk>/', VehiculoDetailView.as_view(), name="VehiculoDetail"),
    path('vehiculo/new/', VehiculoCreateView.as_view(), name="VehiculoNew"),
    path('vehiculo/<int:pk>/edit/', VehiculoUpdateView.as_view(), name="VehiculoEdit"),
    path('vehiculo/<int:pk>/delete/', VehiculoDeleteView.as_view(), name="VehiculoDelete"),
    #Cotizacion
    path('cotizacion/', CotizacionListView.as_view(), name="CotizacionList"),
    path('cotizacion/<int:pk>/', CotizacionDetailView.as_view(), name="CotizacionDetail"),
    path('cotizacion/new/', CotizacionCreateView.as_view(), name="CotizacionNew"),

]