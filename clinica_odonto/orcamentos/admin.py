from django.contrib import admin
from .models import Orcamento

# Register your models here.
@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'paciente', 'dentista', 'valor_total', 'status')
    search_fields = ('paciente__nome', 'dentista__nome', 'status')
    list_filter = ('status',)
    ordering = ('-data',)