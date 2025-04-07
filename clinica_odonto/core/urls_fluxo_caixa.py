from django.urls import path
from .views import (
    ListaFluxoCaixaView,
    DetalheFluxoCaixaView,
    AdicionarFluxoCaixaView,
    EditarFluxoCaixaView,
    DeletarFluxoCaixaView,
)

app_name = 'fluxocaixa'

urlpatterns = [
    path('fluxo_caixa/', ListaFluxoCaixaView.as_view(), name='lista_fluxo_caixa'),
    path('fluxo_caixa/<int:pk>/', DetalheFluxoCaixaView.as_view(), name='detalhe_fluxo_caixa'),
    path('adicionar_fluxo_caixa/', AdicionarFluxoCaixaView.as_view(), name='adicionar_fluxo_caixa'),
    path('editar_fluxo_caixa/<int:pk>/', EditarFluxoCaixaView.as_view(), name='editar_fluxo_caixa'),
    path('deletar_fluxo_caixa/<int:pk>/', DeletarFluxoCaixaView.as_view(), name='deletar_fluxo_caixa'),
]