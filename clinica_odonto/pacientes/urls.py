from django.urls import path
from .views import (
    ListaPacientesView,
    DetalhePacienteView,
    AdicionarPacienteView,
    EditarPacienteView,
    DeletarPacienteView,
    LoginView
)

app_name = 'pacientes'  # Namespace para as URLs

urlpatterns = [
    # Lista todos os pacientes
    path('', LoginView.as_view(), name='login'),
    
    path('pacientes/', ListaPacientesView.as_view(), name='lista_pacientes'),  
    # Detalhes de um paciente específico
    path('<int:pk>/', DetalhePacienteView.as_view(), name='detalhe_paciente'),
    
    # Adicionar novo paciente
    path('adicionar/', AdicionarPacienteView.as_view(), name='adicionar_paciente'),
    
    # Editar paciente existente
    path('<int:pk>/editar/', EditarPacienteView.as_view(), name='editar_paciente'),
    
    # Deletar paciente
    path('<int:pk>/deletar/', DeletarPacienteView.as_view(), name='deletar_paciente'),
]