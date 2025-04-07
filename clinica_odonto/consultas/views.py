from datetime import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Para proteger as views
from django.contrib import messages
from .models import Consulta
from .forms import ConsultaForm


class ListaConsultasView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'consultas/lista_consultas.html'
    context_object_name = 'consultas'
    ordering = ['-data_hora']  # Ordena pela data da consulta em ordem decrescente
    paginate_by = 10  # Número de consultas por página

class DetalheConsultaView(LoginRequiredMixin, DetailView):
    model = Consulta
    template_name = 'consultas/detalhe_consulta.html'
    context_object_name = 'consulta'
    # Aqui você pode adicionar métodos adicionais, se necessário


class AdicionarConsultaView(LoginRequiredMixin, CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/adicionar_consulta.html'
    success_url = reverse_lazy('consultas:lista_consultas')

    def form_valid(self, form):
        # Verifica a data da consulta e se é no passado
        # Se a data da consulta for no passado, adiciona um erro ao formulário
        if form.cleaned_data['data_consulta'] < timezone.now():
            form.add_error('data_consulta', 'Não é possível marcar consultas no passado.')
            return self.form_invalid(form)
        else:
            # Aqui você pode adicionar lógica adicional antes de salvar o formulário
            # Verificar se o paciente já tem uma consulta marcada para a mesma data
            consulta = form.save(commit=False)
            consulta.save()
            messages.success(self.request, "Consulta marcada com sucesso!")
            return super().form_valid(form)


class EditarConsultaView(LoginRequiredMixin, UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/editar_consulta.html'
    success_url = reverse_lazy('consultas:lista_consultas')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar o formulário
        messages.success(self.request, "Consulta editada com sucesso!")
        return super().form_valid(form)


class DeletarConsultaView(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = 'consultas/deletar_consulta.html'
    context_object_name = 'consulta'
    success_url = reverse_lazy('consultas:lista_consultas')

    def delete(self, request, *args, **kwargs):
        # Aqui você pode adicionar lógica adicional antes de deletar o objeto
        messages.success(request, "Consulta deletada com sucesso!")
        return super().delete(request, *args, **kwargs)
    

