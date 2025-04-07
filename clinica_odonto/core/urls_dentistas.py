from django.urls import path
from .views import (
    ListaDentistasView,
    DetalheDentistaView,
    AdicionarDentistaView,
    EditarDentistaView,
    DeletarDentistaView,
)
app_name = 'dentistas'

urlpatterns = [
    path('dentistas/', ListaDentistasView.as_view(), name='lista_dentistas'),
    path('dentista/<int:pk>/', DetalheDentistaView.as_view(), name='detalhe_dentista'),
    path('adicionar_dentista/', AdicionarDentistaView.as_view(), name='adicionar_dentista'),
    path('editar_dentista/<int:pk>/', EditarDentistaView.as_view(), name='editar_dentista'),
    path('deletar_dentista/<int:pk>/', DeletarDentistaView.as_view(), name='deletar_dentista'),
]