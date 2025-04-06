from django.contrib import admin
from .models import Dentista, FluxoCaixa

# Register your models here.
@admin.register(Dentista)
class DentistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade', 'telefone', 'email', 'endereco', 'ativo', 'data_cadastro')
    search_fields = ('nome', 'crm', 'especialidade')
    list_filter = ('ativo', 'especialidade')

@admin.register(FluxoCaixa)
class FluxoCaixaAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao', 'valor', 'tipo', 'dentista')
    search_fields = ('descricao', 'dentista__nome')
    list_filter = ('tipo', 'data')