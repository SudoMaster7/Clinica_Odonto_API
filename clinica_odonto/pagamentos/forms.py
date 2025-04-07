from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'
        widgets = {
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
            'valor_pago': forms.NumberInput(attrs={'step': '0.01'}),
            'forma_pagamento': forms.Select(choices=Pagamento.FORMA_PAGAMENTO_CHOICES),
            'observacoes': forms.Textarea(attrs={'rows': 3})
        }
        labels = {
            'data_pagamento': 'Data do Pagamento',
            'valor_pago': 'Valor Pago',
            'forma_pagamento': 'Forma de Pagamento',
            'observacoes': 'Observações'
        }
        help_texts = {
            'data_pagamento': 'Selecione a data do pagamento.',
            'valor_pago': 'Informe o valor pago.',
            'forma_pagamento': 'Selecione a forma de pagamento utilizada.',
            'observacoes': 'Adicione observações relevantes sobre o pagamento.'
        }
        error_messages = {
            'data_pagamento': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Data inválida.',
            },
            'valor_pago': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Valor inválido.',
            },
            'observacoes': {
                'max_length': 'As observações não podem exceder 500 caracteres.',
            },
        }
        # Adicionando validação personalizada