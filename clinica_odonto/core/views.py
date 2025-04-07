from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Para proteger as views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Dentista, FluxoCaixa
from .forms import DentistaForm, FluxoCaixaForm
from django.utils import timezone # Para verificar a data da consulta
from django.db.models import Sum

@login_required
def HomeView(request):
    return render(request, 'core/home.html')

class ListaDentistasView(LoginRequiredMixin, ListView):
    model = Dentista
    template_name = 'dentistas/lista_dentistas.html'
    context_object_name = 'dentistas'
    ordering = ['nome']  # Ordena pela data da consulta em ordem decrescente
    paginate_by = 10  # Número de consultas por página

class DetalheDentistaView(LoginRequiredMixin, DetailView):
    model = Dentista
    template_name = 'dentistas/detalhe_dentista.html'
    context_object_name = 'dentista'
    # Aqui você pode adicionar métodos adicionais, se necessário


class AdicionarDentistaView(LoginRequiredMixin, CreateView):
    model = Dentista
    form_class = DentistaForm
    template_name = 'dentistas/adicionar_dentista.html'
    success_url = reverse_lazy('dentistas:lista_dentistas')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar o formulário
        messages.success(self.request, "Dentista adicionado com sucesso!")
        return super().form_valid(form)


class EditarDentistaView(LoginRequiredMixin, UpdateView):
    model = Dentista
    form_class = DentistaForm
    template_name = 'dentistas/editar_dentista.html'
    success_url = reverse_lazy('dentistas:lista_dentistas')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar o formulário
        messages.success(self.request, "Dentista editado com sucesso!")
        return super().form_valid(form)
    

class DeletarDentistaView(LoginRequiredMixin, DeleteView):
    model = Dentista
    template_name = 'dentistas/deletar_dentista.html'
    success_url = reverse_lazy('dentistas:lista_dentistas')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Dentista deletado com sucesso!")
        return super().delete(request, *args, **kwargs)
    

class ListaFluxoCaixaView(LoginRequiredMixin, ListView):
    model = FluxoCaixa
    template_name = 'fluxo_caixa/lista_fluxo_caixa.html'
    context_object_name = 'fluxo_caixa'
    ordering = ['-data']  # Ordena pela data em ordem decrescente
    paginate_by = 10  # Número de consultas por página


class DetalheFluxoCaixaView(LoginRequiredMixin, DetailView):
    model = FluxoCaixa
    template_name = 'fluxo_caixa/detalhe_fluxo_caixa.html'
    context_object_name = 'fluxo_caixa'
    # Aqui você pode adicionar métodos adicionais, se necessário


class AdicionarFluxoCaixaView(LoginRequiredMixin, CreateView):
    model = FluxoCaixa
    form_class = FluxoCaixaForm
    template_name = 'fluxo_caixa/adicionar_fluxo_caixa.html'
    success_url = reverse_lazy('fluxo_caixa:lista_fluxo_caixa')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar o formulário
        messages.success(self.request, "Fluxo de caixa adicionado com sucesso!")
        return super().form_valid(form)
    

class EditarFluxoCaixaView(LoginRequiredMixin, UpdateView):
    model = FluxoCaixa
    form_class = FluxoCaixaForm
    template_name = 'fluxo_caixa/editar_fluxo_caixa.html'
    success_url = reverse_lazy('fluxo_caixa:lista_fluxo_caixa')

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional antes de salvar o formulário
        messages.success(self.request, "Fluxo de caixa editado com sucesso!")
        return super().form_valid(form)


class DeletarFluxoCaixaView(LoginRequiredMixin, DeleteView):
    model = FluxoCaixa
    template_name = 'fluxo_caixa/deletar_fluxo_caixa.html'
    success_url = reverse_lazy('fluxo_caixa:lista_fluxo_caixa')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Fluxo de caixa deletado com sucesso!")
        return super().delete(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        # Aqui você pode adicionar a lógica para obter os dados necessários para o dashboard
        # Exemplo: total de consultas, total de dentistas, etc.
        total_dentistas = Dentista.objects.count()
        total_fluxo_caixa = FluxoCaixa.objects.aggregate(Sum('valor'))['valor__sum'] or 0

        context = {
            'total_dentistas': total_dentistas,
            'total_fluxo_caixa': total_fluxo_caixa,
        }
        return render(request, self.template_name, context)

