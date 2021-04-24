from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Registro
# Create your views here.
from django.http import HttpResponse
from shlex import quote
from djbrut import Attempt
import glob


def index(request):

    return render(request, 'exemplo/index.html')


def login_view(request):
    attempt = Attempt('login', request)
    if not attempt.check():
        return HttpResponse(attempt.error)
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        username = None
        password = ''
    next_url = request.GET['next'] if 'next' in request.GET else None
    contexto = {'message': 'insira seus dados'

                }

    if username:
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('entro')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/restrito/')
        else:
            contexto['message'] = 'usuário/senha inválidos'
    return render(request, 'exemplo/login.html', contexto)


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def restrito(request):
    return render(request, 'exemplo/restrito.html')


def pre_sql_safe(request):
    contexto = {
        'vuln': "sql_injection_mitigated",
        'tit': "Lista de projetos",
    }
    latest_registro_list = Registro.objects.order_by('-data_registro')[:10]
    contexto['latest_registro_list'] = latest_registro_list
    return render(request, 'exemplo/pre_sql_safe.html', contexto)


def sql_safe(request, registro_id):
    contexto = {
        'vuln': "sql_injection_mitigated",
        'tit': "Lista de tarefas",
    }
    contexto['registro'] = get_object_or_404(Registro, pk=registro_id)
    return render(request, 'exemplo/sql_safe.html', contexto)


def command_safe(request):
    contexto = {
        'vuln': "command_injection_mitigated",
        'tit': "Pesquisar documentos",
        'result': [],
    }
    try:
        param = request.POST['param']
        if param:
            param = quote(param)
            contexto['param'] = param
            files = '/tmp/uploads/*{}*'.format(param)
            lista = glob.glob(files)
            for entry in lista:
                contexto['result'].append(entry)

    except KeyError:
        contexto['param'] = ''

    return render(request, 'exemplo/command_safe.html', contexto)


def pesquisa_exemplo(request):
    try:
        param = request.POST['param']
        print(param)
        contexto = {'param': param}
    except KeyError:
        contexto = {'param': ''}

    return render(request, 'exemplo/pesquisa_exemplo.html', contexto)


def padrao(request, parametro):
    return HttpResponse("Página não encontrada para: %s." % parametro)
