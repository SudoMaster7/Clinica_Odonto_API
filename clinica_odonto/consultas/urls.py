from django.urls import path
from .views import (
    ListaConsultasView,
    DetalheConsultaView,
    AdicionarConsultaView,
    EditarConsultaView,
    DeletarConsultaView,
)

app_name = 'consultas'

urlpatterns = [
    path('', ListaConsultasView.as_view(), name='lista_consultas'),
    path('consulta/<int:pk>/', DetalheConsultaView.as_view(), name='detalhe_consulta'),
    path('adicionar/', AdicionarConsultaView.as_view(), name='adicionar_consulta'),
    path('editar/<int:pk>/', EditarConsultaView.as_view(), name='editar_consulta'),
    path('deletar/<int:pk>/', DeletarConsultaView.as_view(), name='deletar_consulta'),
]
