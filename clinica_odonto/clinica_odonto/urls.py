from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pacientes.urls', namespace='pacientes')),
    path('admin/', admin.site.urls),
]