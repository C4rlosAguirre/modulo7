from django.db import models


cli_status = [
    (1, 'Cliente'),
    (2, 'Administrador')
]

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, blank='true', null='True')
    apellido = models.CharField(max_length=50, blank='true', null='True')
    edad = models.IntegerField(blank='true', null='True')
    email = models.EmailField(verbose_name="mail del cliente", blank='true', null='True')
    fecha_contratacion = models.DateField(blank='true', null='True')
    clave = models.CharField(max_length=8, blank='true', null='True')
    status = models.IntegerField(
        null=False, blank=False,
        choices=cli_status,
        default=1
    )
    

    def __str__(self):
        return self.apellido
        

        
#class Producto(models.Model):
 #   nombre = models.CharField(max_length=20)

  #  def __str__(self):
   #     return self.nombre
vip_status = [
    (1, 'Premium'),
    (2, 'VIP')
] 

class ClienteVip(models.Model):
    nombre = models.CharField(max_length=50, blank='true', null='True')
    apellido = models.CharField(max_length=50, blank='true', null='True')
    edad = models.IntegerField(blank='true', null='True')
    email = models.EmailField(verbose_name="mail del cliente", blank='true', null='True')
    fecha_registro = models.DateField(blank='true', null='True')
    fecha_nacimiento = models.DateField(blank='true', null='True')
    clave = models.CharField(max_length=8, blank='true', null='True')
    status = models.IntegerField(
        null=True, blank=True,
        choices=vip_status
    )

    def __str__(self):
        return self.apellido
        