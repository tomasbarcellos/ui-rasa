from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('criar/historia', views.criar_historia, name='criar_historia'),
    path('listar/historia', views.listar_historia, name='listar_historia'),
    re_path(r'^criar/(?P<tipo>(acao|intencao))$', views.criar_acao_intencao, name='criar_acao_intencao'),
    re_path(r'^listar/(?P<tipo>(acao|intencao))$', views.listar_acoesintencoes, name='listar_acoes'),
]
