from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "SupermercadoApp/index.html")

def about(request):
    return render(request, "SupermercadoApp/about.html")

def clientes(request):
    return render(request, "SupermercadoApp/clientes.html")

def proveedores(request):
    return render(request, "SupermercadoApp/proveedores.html")

def productos(request):
    return render(request, "SupermercadoApp/productos.html")

def empleados(request):
    return render(request, "SupermercadoApp/empleados.html")