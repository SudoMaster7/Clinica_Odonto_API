from django.urls import path
from .views import ListaPagamentosView, DetalhePagamentoView, AdicionarPagamentoView, EditarPagamentoView, DeletarPagamentoView

app_name = 'pagamentos'

urlpatterns = [
    path('pagamentos/', ListaPagamentosView.as_view(), name='lista_pagamentos'),
    path('pagamento/<int:pk>/', DetalhePagamentoView.as_view(), name='detalhe_pagamento'),
    path('adicionar_pagamento/', AdicionarPagamentoView.as_view(), name='adicionar_pagamento'),
    path('editar_pagamento/<int:pk>/', EditarPagamentoView.as_view(), name='editar_pagamento'),
    path('deletar_pagamento/<int:pk>/', DeletarPagamentoView.as_view(), name='deletar_pagamento'),
]