from flask import Flask, request, render_template, make_response
import subprocess
import pathlib
from shlex import quote
from banco_teste import BancoTeste

"""
ATENÇÃO: Este código é propositalmente vulnerável,
para fins de estudo de programação segura
--------------------------------------------------
TCC CyberSecurity PucPR 1Sem2019
"""

DIR = pathlib.Path(__file__).parent.absolute()
app = Flask(__name__)

template_vulneravel = '''
<html lang=”pt-br”>
    <head>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
        <link href="/static/css/all.min.css" rel="stylesheet" media="screen">

        <script src="/static/js/all.min.js"></script>
        <script src="/static/js/bootstrap.min.js"></script>
        <title>TCC CyberSecurity PUCPR 1ºSem2019</title>
    </head>
    <body>
<br />
<div class="container-fluid">
  <div class="row">
    <div class="col-3">
      <img src="/static/images/logo_trabalho.svg" width="100%" alt="">
    </div>

    <div class="col-9">
    <ol class="breadcrumb">
          <li class="breadcrumb-item"><i class="fas fa-home"></i> <a href="/">Home</a></li>
          <li class="breadcrumb-item active">{vuln}</li>
    </ol>
    <p>Demonstração de vulnerabilidade: <strong class="text-danger">{vuln}</strong></p>
    <br />
    <div class="row">
    <div class="col-5">
        <form method="post" class="form">
          <div class="form-group">
            <label for="cp1">{tit}</label>
            <input type="text" name="param" class="form-control" id="cp1" placeholder="pesquisar...">
            <br />
            <input type="submit" value="Pesquisar" class="btn btn-info"/>
          </div>
        </form>
    </div>
    <div class="col-7">
        <p>Resultados para {param}:</p>
        <br/>
        <pre> {resultado} </pre>
    </div>

    </div>

  </div>

</div>
<div style="text-align:center;padding:0px auto;margin-bottom:1px"><footer><small> TCC CyberSecurity PUCPR 1Sem2019 - Apesentação em 24 de abril de 2021</small></footer></div>
</body>

</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/xss_ok/', methods=['GET', 'POST'])
def xss_ok():
    param = ""
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
    return render_template('xss_ok.html', param=param)


@app.route('/xss_vuln/', methods=['GET', 'POST'])
def xss_vuln():
    param = ""
    vuln = "xss"
    tit = "Informe termo para pesquisa"
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
    return template_vulneravel.format(param=param, tit=tit, vuln=vuln, resultado='')


@app.route('/command_vuln_ok/', methods=['GET', 'POST'])
@app.route('/command_vuln/', methods=['GET', 'POST'])
def command_vuln():
    rule = request.url_rule
    param = ""
    result = b""
    vuln = "command_injection"
    tit = "Pesquisar documentos"
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
        if 'command_vuln_ok' in rule.rule:
            param = quote(param)
        comando = "find ./uploads -iname {}*.pdf".format(param)
        result = subprocess.check_output(comando, shell=True)

    return render_template('command_vuln.html', tit=tit, vuln=vuln, param=param, resultado=result.decode('utf-8'))


@app.route('/login-sql/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def broken_auth():
    rule = request.url_rule
    teste = request.cookies.get('auth_status')
    user = ''
    vuln = "broken_authentication"
    if 'sql' in rule.rule:
        vuln = "sql_injection"
    tit = "Realizar login"
    status = False
    if teste == '_123454':
        status = True
    if request.method == 'POST' and 'user' in request.form.keys() and not status:
        user = request.form['user']
        passwd = request.form['passwd']
        if user == "admin" and passwd == "Admin123":
            status = True
            resp = make_response(render_template(
                'broken_auth.html', vuln=vuln, tit=tit, user=user, status=status))
            resp.set_cookie('auth_status', '_123454')
            return resp
        else:
            tit = "Usuário/Senha inválidos!"
    return render_template('broken_auth.html', vuln=vuln, tit=tit, user=user, status=status)


@app.route('/teste-ldap/', methods=['GET'])
def ldap_injection():
    vuln = "ldap_injection"
    tit = "Pesquisar catálogo"
    return render_template('ldap_injection.html', vuln=vuln, tit=tit)


@app.route('/logout/', methods=['GET'])
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('auth_status', '_____')
    return resp


@app.route('/projetos/', methods=['GET'])
def pre_sql_injection():
    banco_teste = BancoTeste()
    projetos = banco_teste.listar_projetos()
    vuln = "sql_injection"
    tit = "Lista de projetos"

    return render_template('pre_sql_injection.html', vuln=vuln, tit=tit, projetos=projetos)


@app.route('/projeto', strict_slashes=False, methods=['GET'])
def sql_injection():
    '''
    9 union select 1,2,3,4,5,6,(select usuario ||'@@@' || passwd from usuarios where id =1 )
    '''
    projeto_id = request.args.get('projeto_id')
    print(projeto_id)
    tarefas = ()
    banco_teste = BancoTeste()
    if projeto_id:
        tarefas = banco_teste.pesquisar_tarefas_projeto(projeto_id)
    vuln = "sql_injection"
    tit = "Lista de tarefas"

    return render_template('sql_injection.html', vuln=vuln, tit=tit, tarefas=tarefas)
