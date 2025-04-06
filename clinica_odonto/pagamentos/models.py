from django.db import models
from consultas.models import Consulta
from core.models import Dentista
from pacientes.models import Paciente


# Create your models here.
class Pagamento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=50, choices=[('dinheiro', 'Dinheiro'), ('cartao', 'Cartão'), ('pix', 'Pix')])
    status = models.CharField(max_length=20, choices=[('pago', 'Pago'), ('pendente', 'Pendente')])

    def __str__(self):
        return f"Pagamento {self.id} - {self.paciente} - {self.valor_pago}"