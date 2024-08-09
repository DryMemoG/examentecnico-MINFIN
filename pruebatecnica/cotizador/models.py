from django.db import models
from django.utils import timezone
# Create your models here.
class Cliente(models.Model):
    NIT= models.CharField(primary_key=True, max_length=21)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default="example@example.com")
    telefono = models.CharField(max_length=25, default="+502 2222-2222")
    direccion = models.CharField(max_length=255, default="Ciudad")

    def __str__(self):
        return self.apellidos + ", " + self.nombres

class Vehiculo(models.Model):
    OPCIONES = (('mazda', "Mazda"), ('toyota', "Toyota"), ('honda', "Honda"), ('ford', "Ford"), ('chevrolet', "Chevrolet"), ('bmw', "BMW"), ('audi', "Audi"), ('mercedes', "Mercedes-Benz"), ('volkswagen', "Volkswagen"), ('nissan', "Nissan"))
    idAuto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100, choices=OPCIONES, default="mazda")
    modelo = models.IntegerField()
    linea = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/IMG', null=True)

    def __str__(self):
        return self.marca + " " + self.linea + " " + str(self.modelo)

class Cotizacion(models.Model):
    idCot = models.AutoField(primary_key=True)
    NIT = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idAuto = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now())

    def __str__(self):
        return str(self.NIT) +" - "+str(self.idAuto)

