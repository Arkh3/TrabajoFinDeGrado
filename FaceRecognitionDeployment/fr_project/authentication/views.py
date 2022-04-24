from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .forms import LoginForm 
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import LoginForm, RegisterForm

@require_http_methods(["GET", "POST"])
def login1(request):
    if request.method == "GET":
        return render(request, "login1.html", {"form": LoginForm()})
    
@require_http_methods(["GET", "POST"])
def login2(request):
    if request.method == "GET":
        return render(request, "login2.html", {"form": LoginForm()})
    
    form = LoginForm(request.POST)
    
    if not form.is_valid():
        return HttpResponseBadRequest(f"Error en los datos del formulario: {form.errors}")

    # Toma los datos limpios del formulario
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    
    # Realiza la autenticación
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)  # Registra el usuario en la sesión
        return redirect('/welcome/')
    else:
        return render(request, "error.html")

@require_http_methods(["GET", "POST"]) #Adaptarlo luego un poco a como lo tengo en GIW
def register1(request):
    if request.method == "GET":
        return render(request, "registro1.html", {"form": RegisterForm()})
    
def register2(request):
    if request.method == "GET":
        return render(request, "registro2.html", {})
    
def welcome(request):
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    else:
        return redirect('/')

def logoutUser(request):
    logout(request)  # Elimina el usuario de la sesión
    return redirect('/')

