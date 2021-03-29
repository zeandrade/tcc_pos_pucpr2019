from django.shortcuts import render
from .models import Registro
# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_registro_list = Registro.objects.order_by('-data_registro')[:5]
    contexto = {'latest_registro_list': latest_registro_list}
    return render(request, 'exemplo/index.html', contexto)


def vulneravel(request, parametro):
    return HttpResponse("Buscando resultados para: %s." % parametro)


def ver_registro(request, registro_id):
    return HttpResponse("Mostrando registro Nº %s." % registro_id)


def listar_atuacoes(request, registro_id):
    response = "Lista de atuações no registo Nº %s."
    return HttpResponse(response % registro_id)


def ver_atuacao(request, atuacao_id):
    return HttpResponse("Detalhes da atuação Nº %s." % atuacao_id)


def pesquisa(request):
    try:
        param = request.POST['param']
        print(param)
        contexto = {'param': param}
    except KeyError:
        contexto = {'param': ''}

    return render(request, 'exemplo/pesquisa.html', contexto)
