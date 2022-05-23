from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Cliente, ClienteVip, Contacto
from .forms import ClienteForm, ClienteVipForm, UserRegistrationForm, ContactoForm

# Create your views here.
@login_required

def index(request):

    listado = Cliente.objects.all()
    
    return render(request, 'aplicacion/index.html', {'context':listado})

def formulario(request):
    return render(request,'aplicacion/formulario.html')

def create(request):
    form = ClienteForm(request.POST)
    if request.method == 'POST':
    # print(request.POST)
        

        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.edad = form.cleaned_data['edad']
            cliente.email = form.cleaned_data['email']
            cliente.fecha_contratacion = form.cleaned_data['fecha_contratacion']    
            cliente.clave = form.cleaned_data['clave']
            cliente.save()

        else:
            print('Invalido')
        
        return redirect('/aplicacion')
    
    return render(request, 'aplicacion/create.html', {'form': form}) 

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

        context = {'form':form}
        
    return render(request, 'aplicacion/register.html', context)

def consultaclientes(request):

    #context2 = Cliente.objects.all()

    #context = Cliente.objects.raw('SELECT * FROM aplicacion_cliente')
    #print(context)

    context = ClienteVip.objects.raw("SELECT * FROM aplicacion_clientevip")
    
    return render(request, 'aplicacion/consultaclientes.html', {'context':context})  #,'context2':context2


def crearcliente(request):
    form1 = ClienteVipForm(request.POST)
    if request.method == 'POST':
    # print(request.POST)
        

        if form1.is_valid():
            clientevip = ClienteVip()
            clientevip.nombre = form1.cleaned_data['nombre']
            clientevip.apellido = form1.cleaned_data['apellido']
            clientevip.edad = form1.cleaned_data['edad']
            clientevip.email = form1.cleaned_data['email']
            clientevip.fecha_registro = form1.cleaned_data['fecha_registro']    
            clientevip.fecha_nacimiento = form1.cleaned_data['fecha_nacimiento'] 
            clientevip.clave = form1.cleaned_data['clave']
            clientevip.status = form1.cleaned_data['status']
            clientevip.save()

        else:
            print('Invalido')
        
        return redirect('/aplicacion')
    
    return render(request, 'aplicacion/crearcliente.html', {'form1': form1}) 

def crearcontacto(request):
    form = ContactoForm(request.POST)
    if request.method == 'POST':
    # print(request.POST)
        

            if form.is_valid():
                contacto = Contacto()
                contacto.nombre = form.cleaned_data['nombre']
                contacto.apellido = form.cleaned_data['apellido']
                contacto.correo = form.cleaned_data['correo']
                contacto.comentario = form.cleaned_data['comentario']
                contacto.save()

            else:
                print('Invalido')
        
            return redirect('/aplicacion')
    
    return render(request, 'aplicacion/crearcontacto.html', {'form': form}) 

def listarcontacto(request):
    contacto = Contacto.objects.all()
    return render(request, 'aplicacion/listarcontacto.html', {'contacto':contacto})

def editarcontacto(request, id):
    contacto = Contacto.objects.get(pk=id)
    form = ContactoForm(instance=contacto)
    if request.method == "POST":
        form = ContactoForm(data=request.POST, instance=contacto)
        form.save()
        return redirect('listarcontacto')
    else:
        return render(request, 'aplicacion/editarcontacto.html', {'form': form})  

def eliminarcontacto(request, id):
    contacto = Contacto.objects.get(pk=id)    
    contacto.delete()
    return redirect('listarcontacto')