from django.contrib import admin
from .models import Pagamento

# Register your models here.
@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta', 'data_pagamento', 'valor_pago', 'forma_pagamento', 'status')
    search_fields = ('orcamento__paciente__nome', 'orcamento__dentista__nome', 'status')
    list_filter = ('status',)
    ordering = ('-data_pagamento',)