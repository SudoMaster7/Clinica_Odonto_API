from django.contrib import admin
from .models import Paciente

# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'email', 'endereco', 'data_nascimento', 'data_cadastro', 'ativo', 'saldo_devedor')
    readonly_fields = ('saldo_devedor',)
    search_fields = ('nome', 'cpf', 'telefone', 'email')
    list_filter = ('ativo',)
    ordering = ('-data_cadastro',)
