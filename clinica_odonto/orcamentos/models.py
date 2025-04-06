from django.db import models
from core.models import Dentista
from pacientes.models import Paciente

# Create your models here.
class Orcamento(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    procedimentos = models.TextField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('rejeitado', 'Rejeitado')])
    descricao = models.TextField()

    def __str__(self):
        return f"Orçamento {self.id} - {self.paciente} - {self.valor_total}"