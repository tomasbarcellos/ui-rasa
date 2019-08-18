from django.urls import path
from . import views

urlpatterns = [
    path('', views.historia, name='historia'),
    path('historia', views.criar_historia, name='criar_historia'),
    path('intencao', views.criar_intencao, name='intencao'),
    path('acao', views.criar_acao, name='acao'),
]
