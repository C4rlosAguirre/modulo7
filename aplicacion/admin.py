from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.ClienteVip)
admin.site.register(models.Proveedor)
admin.site.register(models.Contacto)
#admin.site.register(models.Producto)