from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .forms import usuarioFormulario,articuloFormulario
from django.contrib.auth.decorators import login_required
from .models import Articulo,Estado
# Create your views here.

def index(request):
    context = {}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    return render(request, "aplicacion/index.html",context)

def nosotros(request):
    context = {}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    return render(request, "aplicacion/nosotros.html",context)

def catalogo(request):
    context = {}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    return render(request, "aplicacion/catalogo.html",context)

def iniciar_sesion(request):
    if request.method == "POST":
        context = {}
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            return render(request, "Aplicacion/login.html",context)
    else:
        context = {}
        return render(request,"aplicacion/login.html",context)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect(index)


def registro(request):
    if request.method == 'POST':
        context = {}
        try:
            if request.POST["password1"] == request.POST["password2"]:
                form = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"],is_active=False)
                form.save()
                return redirect(perfil)
            else:
                formulario = UserCreationForm()
                context["form"] = formulario
            return render(request, "aplicacion/registro.html",context)
        except:
            formulario = UserCreationForm()
            context["form"] = formulario
            return render(request, "aplicacion/registro.html",context)
    else:
        context = {}
        formulario = UserCreationForm()
        context["form"] = formulario
        return render(request, "aplicacion/registro.html",context)

@login_required
def cambio_password(request):
    context = {}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    return render(request, "aplicacion/cambio_password.html",context)

@login_required
def perfil(request):
    context = {}
    if request.method == 'POST':
        try:
            context
            if request.user.is_authenticated :
                context["username"] = request.user.username

            usuario = User.objects.get(username=request.user.username)
            formulario = usuarioFormulario(request.POST,instance=usuario)
            formulario.save()
            return redirect(index)
        except:
            if request.user.is_authenticated :
                context["username"] = request.user.username

            usuario = User.objects.get(username=request.user.username)
            formulario = usuarioFormulario(instance=usuario)
            context["formulario"] = formulario
            return render(request, "aplicacion/perfil.html",context)
    else:
        if request.user.is_authenticated :
            context["username"] = request.user.username

        usuario = User.objects.get(username=request.user.username)
        formulario = usuarioFormulario(instance=usuario)
        context["formulario"] = formulario
        return render(request, "aplicacion/perfil.html",context)

def recuperar_password(request):
    return redirect(index)

def error_404(request, exception):
    return redirect(index)

@login_required
def arte(request):
    context = {}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    articulos = Articulo.objects.filter(idUsuario=request.user)
    context["articulos"] = articulos
    return render(request,'arte/lista.html',context)

@login_required
def arte_add(request):
    context = {}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    if request.method == "POST":
        estado = Estado.objects.get(idEstado='1')
        form = articuloFormulario(request.POST,request.FILES)        
        if form.is_valid():
            articulo_f =  form.save(commit=False)
            articulo_f.idUsuario = request.user
            form.save()
            
            return redirect(arte)
        else:
            print(form.errors)
            articulo = articuloFormulario(instance=estado)
            context["formulario"] = articulo
            return render(request,"arte/agregar.html",context)
    else:
        articulo = articuloFormulario()
        context["formulario"] = articulo
        return render(request,"arte/agregar.html",context)

@login_required
def arte_edit(request, idArticulo):
    return redirect(arte)