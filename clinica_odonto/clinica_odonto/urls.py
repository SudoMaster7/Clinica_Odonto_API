from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls_home', namespace='home')),
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls', namespace='pacientes')),
    path('consultas/', include('consultas.urls', namespace='consultas')),
    path('fluxocaixa/', include('core.urls_fluxo_caixa', namespace='fluxo_caixa')),
    path('dentistas/', include('core.urls_dentistas', namespace='dentistas')),
    path('orcamentos/', include('orcamentos.urls', namespace='orcamentos')),
    path('pagamentos/', include('pagamentos.urls', namespace='pagamentos')),
]