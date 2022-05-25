from pickle import TRUE
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

class Tienda(models.Model):
    nombre = models.CharField(blank=True, max_length=51)
    direccion = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(blank=True, max_length=50)
    nombrefantasia = models.CharField(blank=True, null=True, max_length=50)
    direccion = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, verbose_name="Contacto")
    familia = models.CharField(blank=True, null=True, max_length=50)
    tienda = models.OneToOneField(Tienda,blank=True,  null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombrefantasia

class Subfamilia(models.Model):
    nombre = models.CharField(blank=True, max_length=50)
    proveedor = models.OneToOneField(Proveedor,blank=True,  null=True, on_delete=models.SET_NULL)
    tienda = models.ManyToManyField(Tienda, blank=True)

    def __str__(self):
        return self.nombre
    

class Contacto(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    apellido = models.CharField(blank=True, max_length=100, verbose_name='Apellido')
    correo = models.EmailField(blank=True, max_length=100, verbose_name='Correo')
    comentario = models.CharField(blank=True, max_length=300, verbose_name='Comentario')
    
    def __str__(self):
        return self.nombre





    