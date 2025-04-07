from django.urls import path
from .views import (HomeView,)

app_name = 'home'

urlpatterns = [
    path('', HomeView, name='home'),
    #path('sobre/', SobreView.as_view(), name='sobre'),
    #path('contato/', ContatoView.as_view(), name='contato'),# Para implementar
    #path('politica-privacidade/', PoliticaPrivacidadeView.as_view(), name='politica_privacidade'),
    #path('termos-uso/', TermosUsoView.as_view(), name='termos_uso'),
]
