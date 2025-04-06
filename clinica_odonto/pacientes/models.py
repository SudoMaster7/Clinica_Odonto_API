from django.db import models

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        default='M',  # Adicione um valor padrão se desejar
        verbose_name='Sexo'
    )
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField()
    alergias = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    @property
    def saldo_devedor(self):
        from pagamentos.models import Pagamento
        from orcamentos.models import Orcamento

        # Calcular o saldo devedor do paciente
        pagamentos = Pagamento.objects.filter(paciente=self, status='pago')
        total_pago = sum(pagamento.valor_pago for pagamento in pagamentos)
        orcamentos = Orcamento.objects.filter(paciente=self, status='pendente')
        total_devido = sum(orcamento.valor_total for orcamento in orcamentos)
        return total_devido - total_pago