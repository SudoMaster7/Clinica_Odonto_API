from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Orcamento
from .forms import OrcamentoForm
from django.contrib.auth.mixins import LoginRequiredMixin  # Para proteger as views
from django.contrib import messages

class ListaOrcamentosView(LoginRequiredMixin, ListView):
    model = Orcamento
    template_name = 'orcamentos/lista_orcamentos.html'
    context_object_name = 'orcamentos'
    ordering = ['-data']  # Ordena pela data do orçamento em ordem decrescente
    paginate_by = 10  # Número de orçamentos por página


class DetalheOrcamentoView(LoginRequiredMixin, DetailView):
    model = Orcamento
    template_name = 'orcamentos/detalhe_orcamento.html'
    context_object_name = 'orcamento'
    # Aqui você pode adicionar métodos adicionais, se necessário


class AdicionarOrcamentoView(LoginRequiredMixin, CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamentos/adicionar_orcamento.html'
    success_url = reverse_lazy('orcamentos:lista_orcamentos')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar o formulário
        messages.success(self.request, "Orçamento adicionado com sucesso!")
        return super().form_valid(form)
    

class EditarOrcamentoView(LoginRequiredMixin, UpdateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamentos/editar_orcamento.html'
    success_url = reverse_lazy('orcamentos:lista_orcamentos')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar o formulário
        messages.success(self.request, "Orçamento editado com sucesso!")
        return super().form_valid(form)


class DeletarOrcamentoView(LoginRequiredMixin, DeleteView):
    model = Orcamento
    template_name = 'orcamentos/deletar_orcamento.html'
    success_url = reverse_lazy('orcamentos:lista_orcamentos')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Orçamento deletado com sucesso!")
        return super().delete(request, *args, **kwargs)
    

