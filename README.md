🦷 Sistema de Gestão Odontológica em Django
📋 Visão Geral
Sistema completo para gestão de pacientes em clínicas odontológicas com CRUD de pacientes, consultas e tratamentos.

🚀 Guia de Instalação
Pré-requisitos
Python 3.10+

Git

PostgreSQL (opcional para produção)

bash
Copy
# Clone o repositório
git clone https://github.com/SudoMaster7/Clinica_Odonto_API.git
cd Clinica_Odonto_API

# Configure ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Instale dependências
pip install -r requirements.txt

# Configure o banco de dados
python manage.py migrate

# Crie superusuário
python manage.py createsuperuser

# Execute o servidor
python manage.py runserver
🏗️ Estrutura do Projeto
Copy
clinica_odonto/
├── pacientes/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
├── templates/
└── manage.py
🔧 Configuração de URLs
pacientes/urls.py
python
Copy
from django.urls import path
from .views import (ListaPacientesView, DetalhePacienteView, 
                   AdicionarPacienteView, EditarPacienteView,
                   DeletarPacienteView)

app_name = 'pacientes'

urlpatterns = [
    path('', ListaPacientesView.as_view(), name='lista_pacientes'),
    path('<int:pk>/', DetalhePacienteView.as_view(), name='detalhe_paciente'),
    path('adicionar/', AdicionarPacienteView.as_view(), name='adicionar_paciente'),
    path('<int:pk>/editar/', EditarPacienteView.as_view(), name='editar_paciente'),
    path('<int:pk>/deletar/', DeletarPacienteView.as_view(), name='deletar_paciente'),
]
🧩 Modelo de Paciente
pacientes/models.py
python
Copy
from django.db import models

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    endereco = models.TextField()
    alergias = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
🎨 Templates Essenciais
base.html (Estrutura principal)
html
Copy
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Clínica Odontológica{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    {% block content %}{% endblock %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
Run HTML
lista_pacientes.html (Listagem)
html
Copy
{% extends 'pacientes/base.html' %}

{% block content %}
<table class="table">
    {% for paciente in pacientes %}
    <tr>
        <td>{{ paciente.nome }}</td>
        <td>
            <a href="{% url 'pacientes:editar_paciente' paciente.id %}" class="btn btn-sm btn-warning">Editar</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% endblock %}
Run HTML
🔄 Comandos Git para Publicação
bash
Copy
# Inicialize o repositório
git init

# Adicione arquivos
git add .

# Commit inicial
git commit -m "Initial commit"

# Conecte ao GitHub (substitua pela sua URL)
git remote add origin https://github.com/SudoMaster7/Clinica_Odonto_API.git

# Envie para o repositório
git push -u origin main
📝 Licença
MIT License - Consulte o arquivo LICENSE para detalhes.
