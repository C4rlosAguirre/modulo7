from itertools import product
from django.urls import path

from . import views

urlpatterns = [

        path('', views.index, name="index"),
        path('formulario/', views.formulario, name='formulario'),
        path('create/', views.create, name='create'),
        path('register/', views.register, name='register'),
        path('consultaclientes/', views.consultaclientes, name='consultaclientes'),
        path('crearcliente/', views.crearcliente, name='crearcliente'),
        path('crearcontacto/', views.crearcontacto, name='crearcontacto'),
        path('listarcontacto/', views.listarcontacto, name='listarcontacto'),
        path('editarcontacto/<int:id>/', views.editarcontacto, name='editarcontacto'),
        path('eliminarcontacto/<int:id>/', views.eliminarcontacto, name='eliminarcontacto'),
]