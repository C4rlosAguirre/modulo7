from itertools import product
from django.urls import path

from . import views

urlpatterns = [

        path('', views.index, name="index"),
        path('formulario/', views.formulario, name='formulario'),
        path('create/', views.create, name='create'),
        path('register/', views.register, name='register'),
        path('consultaclientes/', views.consultaclientes, name='consultaclientes'),
        path('crearclientevip/', views.crearclientevip, name='crearclientevip'),
        path('crearcontacto/', views.crearcontacto, name='crearcontacto'),
        path('listarcontacto/', views.listarcontacto, name='listarcontacto'),
        path('editarcontacto/<int:id>/', views.editarcontacto, name='editarcontacto'),
        path('eliminarcontacto/<int:id>/', views.eliminarcontacto, name='eliminarcontacto'),
        path('crearproveedor/', views.crearproveedor, name='crearproveedor'),
        path('creartienda/', views.creartienda, name='creartienda'),
        path('listarproveedor/', views.listarproveedor, name='listarproveedor'),
        path('editarproveedor/<int:id>/', views.editarproveedor, name='editarproveedor'),
        path('eliminarproveedor/<int:id>/', views.eliminarproveedor, name='eliminarproveedor'),
        path('listarclientevip/', views.listarclientevip, name='listarclientevip'),
        path('editarclientevip/<int:id>/', views.editarclientevip, name='editarclientevip'),
        path('eliminarclientevip/<int:id>/', views.eliminarclientevip, name='eliminarclientevip'),

]