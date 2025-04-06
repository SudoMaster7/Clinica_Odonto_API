from django.contrib import admin
from .models import Consulta
# Register your models here.

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data_hora', 'paciente', 'dentista', 'status')
    search_fields = ('paciente__nome', 'dentista__nome')
    list_filter = ('status','data_hora')