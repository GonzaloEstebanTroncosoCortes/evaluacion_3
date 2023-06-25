from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required # 2 importamos el decorador para que solo los usuarios logueados puedan acceder a la vista
from django.contrib.auth import logout
from .models import fotografia
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login



# Create your views here.
def index(request):# creamos esta funcion para cargar la vista para llamar al index por medio del request
    return render(request, 'app/index.html')

def formulario_1(request):# creamos esta funcion para cargar la vista para llamar al formulario_1 por medio del request
    return render(request, 'app/formulario_1.html')

def Mapa(request):# creamos esta funcion para cargar la vista para llamar al formulario_1 por medio del request
    return render(request, 'app/Mapa.html')

def Galeria(request):# creamos esta funcion para cargar la vista para llamar al formulario_1 por medio del request
    return render(request, 'app/Galeria.html')

def nosotros(request):# creamos esta funcion para cargar la vista para llamar al formulario_1 por medio del request
    return render(request, 'app/nosotros.html')

def home(request):# creamos esta funcion para cargar la vista para llamar al formulario_1 por medio del request
    return render(request, 'app/home.html')
# aplicaciones

def agregarProducto(request):
    return render(request, 'app/agregarProducto.html')

def agregarrec(request):
    x=request.POST["nombre"]
    y=request.POST["descripcion"]
    z=request.FILES["archivo_fotografia"]
    foto=fotografia(nombre=x, descripcion=y, archivo_fotografia=z)
    foto.save()
    return redirect(to="ListaProducto")

def eliminar(request, id):
    foto=fotografia.objects.get(id=id)
    foto.delete()
    return redirect(to="ListaProducto")
    
                    
def actualizarProducto(request, id):
    foto=fotografia.objects.get(id=id)
    return render(request, 'app/actualizarProducto.html', {'foto':foto})

def actualizarrec(request, id):
    x=request.POST["nombre"]
    y=request.POST["descripcion"]
    z=request.FILES["archivo_fotografia"]
    foto=fotografia.objects.get(id=id) 
    foto.nombre=x
    foto.descripcion=y
    foto.archivo_fotografia=z
    foto.save()
    return redirect(to="ListaProducto")
@login_required
def ListaProducto(request):
    foto=fotografia.objects.all()
    return render(request, 'app/ListaProducto.html', {'foto':foto})


def exit(request):
    logout(request)
    return redirect(to="ListaProducto")

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
    return render(request, 'registration/register.html',data)