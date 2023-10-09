from django.contrib import admin
from django.urls import path, include
from SupermercadoApp.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="Inicio"),
    path("SupermercadoApp/", include("SupermercadoApp.urls")),
]
