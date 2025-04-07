from django.urls import path
from .views import ListaOrcamentosView, DetalheOrcamentoView, AdicionarOrcamentoView, EditarOrcamentoView, DeletarOrcamentoView

app_name = 'orcamentos'

urlpatterns = [
    path('orcamentos/', ListaOrcamentosView.as_view(), name='lista_orcamentos'),
    path('orcamento/<int:pk>/', DetalheOrcamentoView.as_view(), name='detalhe_orcamento'),
    path('adicionar_orcamento/', AdicionarOrcamentoView.as_view(), name='adicionar_orcamento'),
    path('editar_orcamento/<int:pk>/', EditarOrcamentoView.as_view(), name='editar_orcamento'),
    path('deletar_orcamento/<int:pk>/', DeletarOrcamentoView.as_view(), name='deletar_orcamento'),
]
