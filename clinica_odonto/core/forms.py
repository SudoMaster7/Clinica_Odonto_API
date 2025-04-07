from django import forms
from .models import Dentista, FluxoCaixa

class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentista
        fields = '__all__'
        widgets = {
            'data_cadastro': forms.DateInput(attrs={'type': 'date'}),
            'telefone': forms.TextInput(attrs={'type': 'tel'}),
            'email': forms.EmailInput(),
            'endereco': forms.Textarea(attrs={'rows': 3}),
            'especialidade': forms.TextInput(),
            'crm': forms.TextInput(),
            'nome': forms.TextInput(),
        }
        labels = {
            'nome': 'Nome',
            'crm': 'CRM',
            'especialidade': 'Especialidade',
            'telefone': 'Telefone',
            'email': 'Email',
            'endereco': 'Endereço',
            'ativo': 'Ativo',
        }

class FluxoCaixaForm(forms.ModelForm):
    class Meta:
        model = FluxoCaixa
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.TextInput(),
            'valor': forms.NumberInput(attrs={'step': '0.01'}),
            'tipo': forms.Select(choices=FluxoCaixa.TIPO_CHOICES),
        }
        labels = {
            'data': 'Data',
            'descricao': 'Descrição',
            'valor': 'Valor',
            'tipo': 'Tipo',
        }
        help_texts = {
            'data': 'Selecione a data da transação.',
            'descricao': 'Adicione uma descrição para a transação.',
            'valor': 'Informe o valor da transação.',
            'tipo': 'Selecione o tipo de transação (entrada ou saída).',
        }
        error_messages = {
            'data': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Data inválida.',
            },
            'descricao': {
                'max_length': 'A descrição não pode exceder 255 caracteres.',
            },
            'valor': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Valor inválido.',
            },
        }
        # Adicionando validação personalizada