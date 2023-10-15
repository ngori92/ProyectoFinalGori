from django.contrib import admin
from django.urls import path, include
from SupermercadoApp.views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="Inicio"),
    path("SupermercadoApp/", include("SupermercadoApp.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)