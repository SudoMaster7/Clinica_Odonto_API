from django.db import models

# Create your models here.
class Dentista(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField()
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    #disponibilidade = models.TextField(blank=True, null=True)  # Horários disponíveis


    def __str__(self):
        return self.nome

class FluxoCaixa(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )
    data = models.DateField()
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} - {self.descricao} - {self.valor}"