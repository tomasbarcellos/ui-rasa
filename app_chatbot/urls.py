from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.historia, name='historia'),
    path('historia', views.criar_historia, name='criar_historia'),
    re_path(r'^criar/(?P<tipo>(acao|intencao))$', views.criar_acao_intencao, name='criar_teste'),
]
