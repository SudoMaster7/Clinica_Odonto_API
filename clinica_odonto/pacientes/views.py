# pacientes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin  # Para proteger as views
from .models import Paciente
from .forms import PacienteForm

class ListaPacientesView(LoginRequiredMixin, View):
    def get(self, request):
        pacientes = Paciente.objects.all().order_by('-data_cadastro')
        return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})

class DetalhePacienteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        return render(request, 'pacientes/detalhe_paciente.html', {'paciente': paciente})

class AdicionarPacienteView(LoginRequiredMixin, View):
    def get(self, request):
        form = PacienteForm()
        return render(request, 'pacientes/adicionar_paciente.html', {'form': form})
    
    def post(self, request):
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            # Validação adicional se necessário
            if not paciente.sexo:  # Se o sexo for obrigatório
                messages.error(request, "O campo sexo é obrigatório")
                return render(request, 'pacientes/adicionar_paciente.html', {'form': form})
            
            paciente.save()
            messages.success(request, "Paciente cadastrado com sucesso!")
            return redirect('pacientes:detalhe_paciente', pk=paciente.id)
        
        messages.error(request, "Corrija os erros no formulário")
        return render(request, 'pacientes/adicionar_paciente.html', {'form': form})

class EditarPacienteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(instance=paciente)
        return render(request, 'pacientes/adicionar_paciente.html', {'form': form, 'paciente': paciente})
    
    def post(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, "Paciente atualizado com sucesso!")
            return redirect('pacientes:detalhe_paciente', pk=paciente.id)
        
        messages.error(request, "Corrija os erros no formulário")
        return render(request, 'pacientes/adicionar_paciente.html', {'form': form, 'paciente': paciente})

class DeletarPacienteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.delete()
        messages.success(request, "Paciente removido com sucesso!")
        return redirect('pacientes:lista_pacientes')