from flask import Flask, request, render_template
import subprocess
import pathlib
from shlex import quote
DIR = pathlib.Path(__file__).parent.absolute()
app = Flask(__name__)

template_vulneravel = '''
<html lang=”pt-br”>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/purecss@2.0.5/build/pure-min.css" integrity="sha384-LTIDeidl25h2dPxrB2Ekgc9c7sEC3CWGM6HeFmuDNUjX76Ert4Z4IY714dhZHPLd" crossorigin="anonymous">
        <title>Exemplo Pesquisa</title>
    </head>
    <body>

        <h2 style="color:red;">Exemplo de saída Vulnerável</h2>

    <div class="pure-g">
        <div class="pure-u-12-24">
            <form method="post" class="pure-form">
                <p><input type="text" name="param" placeholder="Informe parâmetro para busca" class="pure-u-20-24" />
                </p>
              <p><input type="submit" value="Pesquisar" class="pure-button pure-button-primary"/></p>
            </form>
        </div>
        <div class="pure-u-12-24"><p>Resultados para {}:</p>
        <pre> {} </pre>
        </div>
        
    </div>
    

    </body>

</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    param = ""
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
    return render_template('index.html', param=param)


@app.route('/xss_vuln', methods=['GET', 'POST'])
def xss_vuln():
    param = ""
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
    return template_vulneravel.format(param, '')


@app.route('/command_vuln', methods=['GET', 'POST'])
def command_vuln():
    param = ""
    result = b""
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
        param = quote(param)
        comando = "find ./uploads -iname {}*.pdf".format(param)
        result = subprocess.check_output(comando, shell=True)

    return template_vulneravel.format(param, result.decode('utf-8'))


@app.route('/code_vuln', methods=['GET', 'POST'])
def code_vuln():
    param = ""
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
    return template_vulneravel.format(param)
