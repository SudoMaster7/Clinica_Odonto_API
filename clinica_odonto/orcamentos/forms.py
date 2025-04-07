from django import forms
from .models import Orcamento

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'valor_total': forms.NumberInput(attrs={'step': '0.01'}),
            'status': forms.Select(choices=Orcamento.STATUS_CHOICES)
        }
        labels = {
            'data': 'Data do Orçamento',
            'descricao': 'Descrição do Orçamento',
            'valor_total': 'Valor Total',
            'status': 'Status'
        }
        help_texts = {
            'data': 'Selecione a data do orçamento.',
            'descricao': 'Adicione uma descrição para o orçamento.',
            'valor_total': 'Informe o valor total do orçamento.',
            'status': 'Selecione o status atual do orçamento.'
        }
        error_messages = {
            'data': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Data inválida.',
            },
            'descricao': {
                'max_length': 'A descrição não pode exceder 500 caracteres.',
            },
        }
        # Adicionando validação personalizada