from django import forms
from .models import Consulta


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date'}),
            'hora_consulta': forms.TimeInput(attrs={'type': 'time'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(choices=Consulta.STATUS_CHOICES)
        }
        labels = {
            'data_consulta': 'Data da Consulta',
            'hora_consulta': 'Hora da Consulta',
            'observacoes': 'Observações',
            'status': 'Status'
        }
        help_texts = {
            'data_consulta': 'Selecione a data da consulta.',
            'hora_consulta': 'Selecione a hora da consulta.',
            'observacoes': 'Adicione observações relevantes sobre a consulta.',
            'status': 'Selecione o status atual da consulta.'
        }
        error_messages = {
            'data_consulta': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Data inválida.',
            },
            'hora_consulta': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Hora inválida.',
            },
            'observacoes': {
                'max_length': 'As observações não podem exceder 500 caracteres.',
            },
        }
        # Adicionando validação personalizada
