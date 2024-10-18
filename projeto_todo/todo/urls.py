from django.urls import path
from .views import atividade_sucesso

urlpatterns = [
    path('erike-nascimento/', atividade_sucesso, name='atividade_sucesso'),
]
