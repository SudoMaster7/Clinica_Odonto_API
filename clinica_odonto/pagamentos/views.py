from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pagamento
from .forms import PagamentoForm


class ListaPagamentosView(LoginRequiredMixin, ListView):
    model = Pagamento
    template_name = 'pagamentos/lista_pagamentos.html'
    context_object_name = 'pagamentos'
    ordering = ['-data_pagamento']  # Ordena os pagamentos pela data de pagamento, do mais recente para o mais antigo
    paginate_by = 10  # Número de pagamentos por página


class DetalhePagamentoView(LoginRequiredMixin, DetailView):
    model = Pagamento
    template_name = 'pagamentos/detalhe_pagamento.html'
    context_object_name = 'pagamento'


class AdicionarPagamentoView(LoginRequiredMixin, CreateView):
    model = Pagamento
    form_class = PagamentoForm
    template_name = 'pagamentos/adicionar_pagamento.html'
    success_url = reverse_lazy('lista_pagamentos')  # Redireciona para a lista de pagamentos após adicionar com sucesso
    
    def form_valid(self, form):
        # Aqui pode atualizar o saldo devedor do paciente, fluxo de caixa, etc.
        # Exemplo: paciente = form.instance.paciente
        # paciente.saldo_devedor -= form.instance.valor_pago
        # paciente.save()
        # Atualizar o fluxo de caixa, se necessário
        # fluxo_caixa = FluxoCaixa.objects.create(valor=form.instance.valor_pago, tipo='entrada')
        # fluxo_caixa.save()
        return super().form_valid(form)


class EditarPagamentoView(LoginRequiredMixin, UpdateView):
    model = Pagamento
    form_class = PagamentoForm
    template_name = 'pagamentos/editar_pagamento.html'
    success_url = reverse_lazy('lista_pagamentos')  # Redireciona para a lista de pagamentos após editar com sucesso

class DeletarPagamentoView(LoginRequiredMixin, DeleteView):
    model = Pagamento
    template_name = 'pagamentos/deletar_pagamento.html'
    success_url = reverse_lazy('lista_pagamentos')  # Redireciona para a lista de pagamentos após deletar com sucesso
    context_object_name = 'pagamento'
