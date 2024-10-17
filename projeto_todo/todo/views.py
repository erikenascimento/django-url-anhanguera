from django.http import HttpResponse

def atividade_sucesso(request):
    return HttpResponse("Realizado com sucesso a atividade")
