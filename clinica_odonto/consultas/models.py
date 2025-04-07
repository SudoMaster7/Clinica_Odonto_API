from django.db import models
from core.models import Dentista
from pacientes.models import Paciente

# Create your models here.
class Consulta(models.Model):
    STATUS_CHOICES = (
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    )
    paciente = models.ForeignKey(Paciente , on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista , on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    procedimento = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('agendada', 'Agendada'), ('realizada', 'Realizada'), ('cancelada', 'Cancelada')])
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente} - {self.data_hora}"