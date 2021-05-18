## Desenvolvimento seguro em linguagem Python para programação Web
_Gabriel Zamproni, José Roberto Andrade Jr_

<small>Pontifícia Universidade Católica do Paraná(PUC-PR), Curitiba, PR – Brazil</small>

<small> Abril de 2021</small>

_**Abstract**_.

    This paper describes techniques and good practices to avoid the main cybersecurity problems and known flaws of web systems, taking as reference the indicators and reports of the main vulnerabilities of the OWASP (Open Web Application Security Project), and apply them to web programs developed in Python language. Through the studies carried out it was possible to demonstrate that the correct validation of the manipulated data, especially of the data inserted by the users in web interfaces, is a key condition to avoid an expressive part of the analyzed vulnerabilities. It was noticed that Python and its development frameworks are equipped with libraries and compiled to prevent the tested vulnerabilities from occurring.

_**Resumo**_. 

    Este artigo descreve técnicas e boas práticas para evitar os principais problemas de cibersegurança e falhas conhecidas de sistemas web, tomando por referência os indicadores e relatórios de principais vulnerabilidades da OWASP (Open Web Application Security Project), e aplicá-las a programas web desenvolvidos em linguagem Python. Através dos estudos realizados foi possível demonstrar que a correta validação dos dados manipulados, em especial dos dados inseridos pelos usuários em interfaces web, é a condição chave para se evitar um parte expressiva das vulnerabilidades analisadas. Percebeu-se que o Python e seus frameworks de desenvolvimento são dotados de bibliotecas e funcionalidades adequadas para evitar a ocorrência das vulnerabilidades testadas.
​
### 1. Introdução
No início das redes de computadores, a interconectividade era realizada entre nós conhecidos entre si, e em ambientes controlados. Com o avanço da conectividade entre softwares de servidores, computadores corporativos e computadores pessoais através da internet, isto tornou as aplicações e dados mais expostos a ameaças cibernéticas, ampliando a necessidade de tornar as aplicações ainda mais seguras, estáveis e confiáveis, tornando constante a preocupação com a segurança da informação. [HOWARD; LEBLANC, 2005]

Diante esse cenário de ameaças crescentes, há a necessidade cada vez maior de profissionais qualificados e capacitados na área de segurança da informação. No entanto, o déficit por esse tipo de profissional pode chegar a 3.5 milhões em 2021, fato que vem gerando preocupação para empresas e agências governamentais relacionadas a área de segurança da informação. [COMPUTERWORLD, 2017]

Na atualidade, tornam-se cada vez mais recorrentes os casos de vazamentos de informações sigilosas e pessoais. A sociedade e governos passam a exigir maior responsabilidade dos cidadãos e empresas através de legislações específicas para o uso e proteção de dados. As ameaças aos computadores são variadas e podem se estender em diversas maneiras de ataque, e uma das principais causas para estes vazamentos são falhas exploradas em aplicações web.

O Open Web Application Security Project (OWASP), que realiza um trabalho de identificação de ameaças cibernéticas e de apoio a melhoria da segurança de aplicações por meio diversos projetos, realiza regularmente a documentação das principais ameaças web através do The OWASP Top Ten Project. [OWASP Top Ten, 2017]

O OWASP Top Ten Project, levantou em sua última versão disponível, que data de 2017, o ranking das dez principais vulnerabilidades de aplicações web, sendo que, independente da tecnologia em que o software tenha sido desenvolvido ele pode estar vulnerável caso não siga boas práticas de desenvolvimento e segurança. O Top Ten então passa a funcionar como um referencial para desenvolvimento e testes de segurança para softwares utilizados na Internet.

Segundo ENISA (European Union Agency for Cybersecurity), no período de Janeiro de 2019 até Abril de 2020, os ataques explorando a parte de aplicações web ocuparam o quarto lugar no ranking de ameaças a computadores e sistemas em todo o mundo. [ENISA, 2020]

As linguagens de programação também aumentaram sua quantidade com o crescimento da conectividade dos computadores, e estão em constante mudança de versões e abrangência das funcionalidades. Entre as inúmeras linguagens de programação está a linguagem Python que, dentre suas diversas funcionalidades, pode ser utilizada para criação de aplicações web. Em 2016, o Python ocupava quinto lugar no ranking de linguagens de programação mais usadas. Em fevereiro de 2021, ocupava a terceira posição demostrando um significativo crescimento em sua popularidade. [TIOBE, 2021]

Assim, uma aplicação web criada em Python pode ser abordada pelas premissas do The OWASP Top Ten Project para minimizar riscos aos seus usuários. Nesse trabalho, inicialmente serão abordadas as principais vulnerabilidades web listadas pela organização OWASP e serão apresentadas propostas de implantação seguras e boas práticas em Python capazes de evitar os ataques descritos neste estudo.
​
### 2. Python
A linguagem Python foi desenvolvida em 1990 e tem como característica ser uma linguagem de alto nível e interpretativa, utilizada para múltiplos propósitos. Composta por diversas estruturas de dados, entre elas: listas e dicionários. Python possui seu código aberto e é distribuído sob licença do tipo GLP (General Public License) permitindo a sua utilização de forma livre e gratuita. [BORGES, 2010]

O Python é voltado para o desenvolvimento ágil e possui suas variáveis dinamicamente tipadas, ou seja, quando declarada uma variável não é necessário definir o tipo primitivo da variável, a própria linguagem é capaz de convertê-lo de acordo com o valor armazenado na variável. A linguagem permite o desenvolvimento tanto em paradigma estruturado quanto orientado a objetos, com uma peculiaridade: a linguagem trata todos os elementos como objetos, mesmo as variáveis de tipo numérico inteiro possuem métodos e atributos. [SILVA;SILVA, 2019] 

Um destaque da linguagem Python é a simplicidade e a legibilidade de sua sintaxe, sendo obrigatório o uso de espaçamento (indentation) para a organização lógica das rotinas e estruturas dos códigos, facilitando a leitura e entendimento dos mesmos. Outra característica marcante é a diversidade de aplicações, estando presente em inúmeras áreas como inteligência artificial, ciência de dados, aplicativos e jogos eletrônicos. [MENEZES,2019] 

A quantidade de bibliotecas da linguagem Python é vasta e adiciona diversas funcionalidades de ajuda aos desenvolvedores. Por exemplo, na biblioteca padrão da linguagem estão as bibliotecas os, sys, subprocess e glob, as quais permitem interações com o sistema operacional do computador. Outra biblioteca útil e instalada por padrão é a collections, a qual, facilita operações com coleções de dados, como, listas e dicionários. [HATTINGH, 2016]

Além da biblioteca padrão existem outras bibliotecas que podem ser adicionadas e frameworks de desenvolvimento. Entre as diversas funcionalidades do Pyhton está o desenvolvimento web, sendo que um framework popular para essa atividade é o Django.

Para os exemplos apresentados neste artigo são compatíveis com a versão 3 do Python, por ser a versão corrente e recomendada para o desenvolvimento de novos aplicativos.
​
#### 2.1. Django
O Django é um framework voltado para entregar de forma rápida e eficiente aplicações web, aplicável tanto a portais simples com projetos de maior complexidade. O Django inclui suporte para diversos bancos de dados externos e possui bases de dados em backend para uso. [MOZILLA, 2020]

Outro destaque do Django são recursos de segurança. O framework possui diversas implementações voltadas para a proteção de ataques comuns. Entre as proteções desse framework estão defesas contra ataques de CSRF (Cross-Site Request Forgery), SQL INJECTION, CSS (Cross-Site Script) e ClickJacking. [SILVA; SILVA, 2019]. Em sua documentação oficial o Django traz um capítulo abordando especificamente otema de segurança, demonstrando sua abordagem para tratamento de diferentes ameaças web.

Nativamente o Django possui mecanismos para autenticação de usuários presente no pacote Django.contrib.auth. Essa ferramenta permite gerir permissões de usuários, criar grupos de usuários, criar hashes de senhas e formulários de logins. [AZZOPARDI; MAXELL, 2016]

A escolha do Django como framework preferencial para o desenvolvimento, e para a apresentação e demonstração de práticas de programação segura deu-se a partir de um breve comparativo entre cinco frameworks web em python, pré selecionados devido à expressividade junto a portais de desenvolvimento, presença de funcionalidades para um desenvolvimento completo de uma aplicação web e qualidade de documentação. Foram comparados: Django, Flask, Web2py, Pyramid e Tornado, considerando a presença de construção de sistemas web e de recursos para segurança da informação no próprio framework ou em módulos totalmente compatíveis. Assim, obtivemos os seguintes dados: 

Tabela 1: características e módulos
Framework
Motor de exibição
ORM para BD
autenticação
Última versão 
Django
próprio
próprio
próprio
3.2.3 – maio/ 2021 
Flask
módulo
módulo
extensão
2.0 – maio /2021
Web2py
próprio
próprio
Próprio, terceiros
2.19.1 - março/2021
Pyramid
plugins e módulos
plugins e módulo
próprio
2.0 – março /2021
Tornado
próprio
plugin
próprio, plugin
61 - outubro/2020

Tabela 2: tratamento de vulnerabilidades e recursos
Framework
CSRF
XSS
SQL Injection
Brute Force
Criptografia
Django
Possui nativo
Possui nativo
Evitado via (ORM)
Via módulo djbrut
Forte: argon2 e pbkdf2
Flask
Via extensão
externo
Externo (ORM)
não
externo
Web2py
Possui nativo
parcial
Evitado via ORM
não
Hmac + sha512
Pyramid
Possui nativo
externo
externo(ORM)
não
bcrypt
Tornado
possui
parcial
externo(ORM)
não
externo
Para as demonstrações utilizando Django presentes neste artigo foi empregada a versão 3.1.7 do framework.
​
### 3. OWASP
Open Web Application Security Project é uma Organização sem Fins Lucrativos, a qual, visa melhorar a segurança de aplicações. Em setembro de 2021, a organização completará seu vigésimo aniversário. Ao longo de sua trajetória foram oferecidos diversos relatórios de vulnerabilidades, análises e treinamentos relacionados à segurança da informação. [OWASP,2017]

O projeto de maior destaque é o OWASP Top Ten, nele são listados os dez principais tipos de ataques contra aplicações web que são exploradas por hackers. A primeira versão do estudo foi publicada em 2003 e mostrou as principais falhas de programação que tornam os sites inseguros. Nos anos de 2004, 2007, 2010 e 2013 foram lançadas novas versões do relatório OWASP Top Ten com atualizações e alertas de brechas de segurança. O levantamento das informações é realizado com o apoio de especialistas em segurança da informação, empresas de tecnologia e organizações governamentais. [CARVALHO,2014] O objetivo do projeto é conscientizar profissionais e organizações da área de desenvolvimento e Tecnologia da Informação dos riscos e consequências que seus códigos estão sujeitos. Ainda, a OWASP oferece dicas e boas práticas para proteção dessas vulnerabilidades. [OWASP,2017]

O relatório mais recente do OWASP Top Ten foi publicado em 2017. Nesse relatório foram analisadas centenas de organizações e mais de cem mil aplicações web. Em seguida, foi montada a lista das dez ameaças mais comuns com base em informações de ocorrência, explorabilidade, detecção e impacto de cada tipo de ameaça. [OWASP,2017]

O relatório final de 2017 apresentou algumas mudanças quando comparado com o relatório de 2013, sendo que, os ataques de XML External Entities (XEE), Insecure Deserialization e Insufficient Logging&Monitoringoram foram adicionados. Ainda, os ataques de Insecure Direct Object References e Missing Function Level Access Control foram unificados em uma categoria. Já as vulnerabilidades de Cross-Site Request Forgery (CSRF) e Unvalidated Redirects and Forwards acabaram sendo removidas da lista de 2017. [OWASP,2017]

Desse modo, as principais ameaças levantadas no último relatório são mostradas de forma decrescente (de A1 até A10) na Tabela 1.

Tabela 3. OWASP Top Ten – 2017

Posição | Vulnerabilidade
------- | ---------------
A1 | Injection
A2 | Broken Authentication
A3 | Sensitive Data Exposure
A4 | XML External Entities (XXE)
A5 | Broken Access Control
A6 | Security Misconfiguration
A7 | Cross-Site Scripting (XSS)
A8 | Insecure Deserialization
A9 | Using Components with Known Vulnerabilities
A10 | Insufficient Logging & Monitoring

Adiante no trabalho será abordado o funcionamento de algumas das vulnerabilidades listadas. Também serão apresentadas propostas de implementação em Python efetivas contra a vulnerabilidade abordada na ocasião.
​
### 4. Vulnerabilidades de Injeção
Agrupam-se na categoria de vulnerabilidades de injeção todo tipo de falha que permita a inserção de códigos indesejados, que serão executados no contexto da aplicação e causarão comportamento inesperado. 

Em geral, esse tipo de falha tem origem na falta de tratamento dos dados de entrada e complementarmente, na falha de tratamento de erros.

Dentre os diversos tipos de ataque explorando vulnerabilidades de injeção, destacam-se para este estudo a injeção de SQL, a injeção de comandos e a injeção LDAP. Tanto o princípio de exploração da vulnerabilidade quanto os princípios para correção e mitigação aplicados à programação em Python assemelham-se para todos esses tipos. Porém, como o potencial e a natureza dos problemas causados em cada variante é diferente, torna-se importante para o estudo detalhar estes tipos de ataque.
​ 
#### 4.1. Injeção de SQL
Um ataque de injeção de SQL consiste na inserção de qualquer consulta SQL parcial ou completa por meio da entrada de dados transmitida do cliente (navegador) para a aplicação WEB. Um ataque bem-sucedido pode acessar dados confidenciais do banco de dados, modificar dados do banco, executar operação de administração no banco de dados, recuperar o conteúdo de um determinado arquivo existente no sistema de arquivos do banco ou do sistema operacional e, dependendo da tecnologia, executar comandos de sistema operacional. Em geral, para composição da consulta SQL, são aproveitadas informações inseridas em formulários da interface com usuário, ou seja, dados externos à aplicação, fornecidos pelo usuário.

Por exemplo, ilustremos uma funcionalidade de sistema web em que o usuário realizará pesquisa para consultar usuário com nome "José". Traduzindo esta funcionalidade em código, uma instrução de consulta em banco de dados espera a informação de um parâmetro para composição da instrução, buscará o valor fornecido no campo "nome" de uma tabela "usuarios". Como este termo informado será incorporado à instrução SQL, um usuário mal-intencionado poderá informar no lugar do parâmetro desejável um trecho de código que altere a instrução SQL originalmente projetada.

Segundo [OWASP Top Ten,2017], ataques de injeção SQL podem ser divididos nas três seguintes classes 

-  Inband: os dados resultantes são extraídos usando a mesma interface que foi usada para injetar o código SQL. Este é o tipo mais direto de ataque, no qual os dados recuperados são apresentados diretamente na tela de exibição da aplicação WEB. 
-  Outband: os dados são recuperados usando uma interface diferente (por exemplo, um e-mail com os resultados da consulta que seja gerado e enviado para o pentester ou um relatório PDF resultante de determinada requisição).
- Inferencial ou cego: não há exposição direta de dados, mas o pentester é capaz de reconstruir as informações enviando solicitações e observando o comportamento resultante da comunicação com o servidor de banco de dados. Um ataque de injeção SQL bem-sucedido exige que o invasor crie uma consulta SQL sintaticamente correta. Se a aplicação web retornar mensagem de erro devido uma consulta incorreta, muitas informações sobre o tipo de erro serão apontadas e será possível ao atacante realizar inúmeras consultas para, através de técnicas de engenharia reversa, descobrir e validar informações da estrutura de banco. 
 
Para exploração das falhas de injeção de SQL, existem cinco técnicas comuns. Ainda, essas técnicas eventualmente podem ser utilizadas de forma combinada (por exemplo, através de operador SQL de união):

- Operador de união: pode ser usado quando a falha de injeção de SQL acontece em uma instrução SELECT, tornando possível combinar duas consultas em um único resultado ou conjunto de resultados. 
- Booleano: utilizar condição(ões) booleana(s) para verificar se determinado as condições são verdadeiras ou falsas.
- Baseado em erros: esta técnica força o banco de dados a gerar um erro, fornecendo ao invasor ou pentester informações que este utilizará para refinar sua injeção.
- Out-of-band: técnica usada para recuperar dados usando um diferente destino (por exemplo, faça uma conexão HTTP para enviar os resultados a um servidor web). 
- Atraso de tempo: através de funções e comandos nativos do banco de dados (por exemplo, o comando sleep) que são utilizados para atrasar as respostas em consultas condicionais. É útil quando o invasor não tem algum tipo visível de resposta da aplicação (resultado em tela ou mensagem de erro). Assim ele avaliará a efetividade do ataque pelo tempo de resposta do comando. 
Testando existência de vulnerabilidade em Python, adaptado do que é detalhado por [PAULI, 2014] para implementar este teste, o passo inicial consiste em entender quando a aplicação WEB interage com um servidor de banco de dados para acessar alguns dados. Isto geralmente acontece em: 
- Formulários de autenticação: quando a autenticação é realizada usando um formulário da web, é provável que as credenciais do usuário sejam verificadas em um banco de dados que contém todos os nomes de usuário e hashes de senha. 
- Mecanismos de busca: a string enviada pelo usuário pode ser usada em uma consulta SQL que extrai todos os registros encontrados no banco de dados para o parâmetro. 
- Sites de comércio eletrônico: os produtos e suas características (preço, descrição, estoque etc.) provavelmente estão armazenados em um banco de dados. O pentester pode aproveitar todo campo de formulário que aceite uma entrada de dados no lado cliente, incluindo também campos de formulário ocultos, dados armazenados em cookies e então, testá-los separadamente tentando interferir na consulta e obter um erro não tratado. 

O primeiro teste geralmente consiste em adicionar uma aspa simples (') ou um ponto e vírgula (;) para valor inserido no campo de formulário ou parâmetro de URL em teste. A aspa simples é utilizada em consultas SQL como um delimitador de strings e, se não for filtrado pela aplicação WEB, levaria a uma consulta incorreta. Já o ponto e vírgula é utilizado para encerrar uma declaração SQL e, se não for filtrada, também é provável que gere um erro. Também é possível utilizar delimitadores de comentário (como -- ou / * * /) e outras palavras-chave SQL como ‘AND’ e ‘OR’ para modificar a consulta.

Para demonstração de falha, observe-se o trecho de código abaixo em que uma função Python vulnerável, destinada a recuperar a informação de uma tabela de banco de dados para validar se determinado usuário é um administrador do sistema:

```python
 def validar_admin(connection, usuario: str) -> bool:
     with connection.cursor() as cursor:
         cursor.execute(
             "SELECT admin FROM usuarios WHERE usuario = '%s'" % usuario)
         result = cursor.fetchone()
     admin = result
     return admin
```
No caso de um teste de injeção, o resultado esperado será manipulado como se observa em:

```python
validar_admin(connection, "'; select true; --")
```
Isto faz com que a instrução enviada ao banco seja traduzida em:

```python
"SELECT admin FROM usuarios WHERE usuario = ''; select true; --'"
```
Assim, devido à vulnerabilidade, o resultado da consulta retornará sempre um valor booleano verdadeiro (True).
 
Para corrigir essas vulnerabilidades usando Python, as melhores práticas de programação recomendadas para manipulação dados que são utilizadas em requisições SQL envolvem:

- Utilizar preferencialmente bibliotecas para abstração de bancos de dados, em que já exista uma coleção de tratamentos de dados de entrada e saída, bem como formas de interação com os dados que já fornecem uma camada de proteção ao banco de dados. Além de agilizar a produtividade do desenvolvedor e padronizar o código, essas bibliotecas são constantemente atualizadas face à sua ampla adoção. Destaca-se para este propósito a biblioteca SQLAlchemy ou no caso do framework Django, seu prórprio ORM nativo.

SQLAlchemy é uma biblioteca para abstração do Banco de Dados, através de mapeamento objeto-relacional. Nela a estrutura de banco de dados é representada em objetos associados às tabelas, as colunas são associados a atributos com as devidas definições e as atividades de manipulação dos registros é realizada através de métodos destes objetos.

Esta biblioteca também implementa as relações entre tabelas, e pode ser utilizada com qualquer banco de dados relacional suportado pelo Python. Isto também facilita a mudança de SGBD se necessário.

O framework Django também possui seu ORM, disponibilizado em django.db.models.Model. Esta classe também realizada a abstração de forma semelhante, associando a cada tabela do banco uma representação em forma de objeto.

Em casos que não admitam a utilização de abstração do banco de dados, faz-se necessária a validação imediata do dado recebido, que pode envolver:
- A validação do tipo de dado, como no caso de um campo que espere exclusivamente a inserção de dados numéricos, consistindo em descartar qualquer valor diferente inserido.
- A validação de strings ou blocos de texto são situação mais trabalhosas e de maior risco. Assim, é necessário o emprego de várias técnicas. Nas situações em que exista um modelo de dados esperado, como em campos em que o dado dever ser um endereço de e-mail, um número de telefone ou login, é possível utilizar expressões regulares para validar se o dado informado corresponde ao modelo esperado. Também é possível fazer a análise da presença de caracteres inválidos através de uma lista proibida, e de forma complementar medir o comprimento da string recebida.
- Fazer o tratamento de mensagens de erro resultantes em requisições SQL, sem jamais permitir a exibição deste erro na interface com o usuário ou nos dados de saída. Porém esta mitigação não é totalmente eficiente, pois atacantes poderiam se valer de ataques inferenciais e testes cegos.

No código abaixo temos um exemplo de abstração de banco de dados através de SQL Alchemy:

```python
 class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(80), unique=True, nullable=False)
     email = db.Column(db.String(120), unique=True, nullable=False)
     admin = db.Column(db.Boolean, nullable=False, default=False)
 
     def __repr__(self):
         return '<User %r>' % self.username
```
E para este modelo, a função nativa de filtro já disponível na biblioteca evita a injeção demonstrada:
```python
User.query.filter_by(admin=True).fetchall()
```
Da mesma forma, o framework Django através de seu ORM nativo tratará de forma adequada situação semelhante, por exemplo num objeto “users”:

```python
 try:     
     user = users.objects.get(category = 'admin')     
     if user:         
         return render(request, 'main/admin.html')    
 except Exception as e:     
        return render(request, 'main/home.html')
```
​
#### 4.2 Injeção LDAP 
Outro tipo de injeção que traz consigo particularidades é a Injeção de comandos LDAP. Em sistemas corporativos é comum favorecer a padronização de identidade dos usuários entre os diversos sistemas. Assim, através da adoção de um sistema de árvore de diretórios, o mesmo usuário poderá ser utilizado em diferentes serviços, mesmo através de métodos de autenticação distintos. A gestão de identidades fica centralizada e as demais aplicações como acesso a estações de trabalho, autenticação em servidores, em dispositivos em sistema intranet e internet entre outros, consomem como clientes esta estrutura de identidades, por exemplo através do protocolo LDAP.

Como neste cenário se encontra o uso do protocolo LDAP em sistemas web, novamente uma falha no tratamento de entrada de dados do tipo string em formulários web causará um comportamento indesejado. Ao informar o usuário ou a senha durante o processo de autenticação, pode tanto gerar um erro de validação quanto, através das técnicas de injeção de trechos de consultas LDAP, ocasionar anomalias no comportamento da aplicação e, dependendo das combinações de consultas, poderiam causar desde sobrecargas no serviço LDAP a autenticação de um usuário aleatório sem a senha.

Assim esta falha de injeção também estaria relacionada com outra vulnerabilidade destaca no OWASP, que é a de quebra de autenticação. Observa-se no exemplo abaixo que a falta de tratamento dos parâmetros recebidos pode causar uma injeção LDAP na função de consulta:

```python
 from ldap3 import Server, Connection, ALL
 
 def bind_simples(usuario, atributos):
     servidor = Server('ldaps://exemplo.dominio', use_ssl=True, get_info=ALL)
     conexao = Connection(servidor, auto_bind=True)
     filtro = '(uid={})'.format(usuario)
     conexao.search('dc=dominio,dc=com,dc=br', filtro, attributes=atributos)
     if len(conexao.response) > 0:
         return conexao.response
     else:
         return []
```

Neste cenário um atacante pode explorar diferentes vetores de ataque, para gerar um abuso sobre as consultas LDAP:

```python
 usuario_ataque = '*'
 usuario_ataque = '*)(|(cn=*)'
 usuario_ataque = '*)(|(mail=*)'
```

Porém a própria biblioteca Python “ldap3” utilizada no exemplo possui funcionalidade para tratar adequadamente o parâmetro antes de executar a consulta:

```python
from ldap3.utils import conv
usuario_ok = conv.escape_filter_chars(usuario_ataque, encoding=None)
atributos = ['dn', 'cn', ‘mail’]
resposta = bind_simples(usuario_ok, atributos)
print(resposta)
```

#### 4.3 Injeções de Código e Injeções de Comando

Programadores de sistemas web podem deparar-se com a necessidade de, através de dados coletados, realizar tarefas de interação com o sistema operacional ou mesmo personalizar trechos de código que serão executados. 

Para uma breve distinção se denomina segundo [OWASP, 2017] injeção de código, a vulnerabilidade em que o atacante consegue implantar trechos da mesma linguagem de programação da aplicação e injeção de comando, a inserção de comandos de sistema operacional do servidor que executa e hospeda a aplicação. 

Mesmo sem o prévio conhecimento de como estas funcionalidades foram projetadas, um atacante pode realizar um pentest inserindo em campos de formulários web comandos de sistema operacional e trechos da linguagem de programação utilizada (caso seja identificada) para tentar interferir no comportamento da aplicação. Mais uma vez a falta de tratamento de dados de entrada pode inserir uma vulnerabilidade a este tipo de ataque. 

A melhor forma de defesa contra estes tipos de injeção segundo [KOHNFELDER; HEYMANN et al. 2018], é o cuidado extremo com o tratamento da string que contém os dados inseridos pelo usuário que será utilizada nestas funcionalidades. Ela não poderá admitir valores que, uma vez passados a comandos a serem executados, possam trazer trechos de instruções shell ou trechos de programas Python. Desta forma, o desenvolvedor python deve evitar ao máximo o uso de funções nativas como eval() e os.system() em sistemas web. Se estas funções forem indispensáveis para o projeto, o parâmetro necessário deve ser facilmente identificável e tratável segundo o padrão esperado em seu escopo de utilização. 

O risco implícito em injeções de código ou injeções de comando envolve desde a possibilidade de impacto direto na performance do servidor da aplicação, travamento da aplicação, abuso de recursos de armazenamento, e até a instalação e execução de códigos maliciosos (como backdoors e artefatos de command and control).

Abaixo demonstra-se o caso de um comando concebido para pesquisar a presença de arquivos PDF em determinado diretório de “uploads”, porém vulnerável a ataques do tipo command injection:

```python
def command_vuln():
    param = ""
    result = b""
    if request.method == 'POST' and 'param' in request.form.keys():
        param = request.form['param']
        comando = "find ./uploads -iname {}*.pdf".format(param)
        result = subprocess.check_output(comando, shell=True)
        return template_vulneravel.format(param, result.decode('utf-8'))
```
Com isso, um atacante pode explorar a vulnerabilidade através da passagem do seguinte parâmetro:

```bash
exemplo; cat /etc/passwd; #
```

O Python provê recurso para o devido tratamento do parâmetro através de sua biblioteca nativa “shlex” que conta com a função “quote”, conforme exemplo corrigido:

```python
from shlex import quote
# (...)
param = request.form['param']
param = quote(param)
comando = "find ./uploads -iname {}*.pdf".format(param)
result = subprocess.check_output(comando, shell=True) 
```

### 5. Broken Authentication
Diversas listas contendo informações de usuários e senhas de websites estão disponíveis para invasores depois de ataques que ocasionaram o vazamento dessas informações. Ainda, falhas no modo em que as sessões web são geridas, ID de sessões expostas nos campos de URL ou métodos inseguros para recuperação de senhas, também contribuem com o sucesso dos criminosos na obtenção indevida de informações sensíveis. Esses dados podem ser utilizados em ataques automatizados à websites deficientes no controle de acesso e burlar os métodos de autenticação, acarretando perdas financeiras, impactos sociais e roubos de credenciais e contas de usuário. [OWASP,2017]
Essa falha de segurança pode ser explorada de diversas maneiras, sendo uma delas o ataque de Força Bruta. Esse ataque é baseado no formato de tentativa e erro, nesse método de exploração o atacante tenta adivinhar o login dos usuários enviando senhas de um dicionário aos formulários web. Senhas fracas cadastradas pelos usuários e a permissão de sites para diversas tentativas de acesso consecutivas ampliam a possibilidade do sucesso desse tipo de ataque. [NAGPAL,2014]
O alcance dos ataques de Força Bruta pode ser amplificado por meio do uso ferramentas de automatização das tentativas de login. Ou seja, ferramentas como Brutus, Medusa e THC Hydra, permitem ao atacante munido de um dicionário de senhas, testar senha a senha na tentativa de violar o acesso. A velocidade dessa verificação de tentativa e erro é aumentada pelo uso de GPU (Unidade de Processamento Gráfico), a qual possui milhares de núcleos capazes de acelerar em cerca de 250 vezes o processamento quando comparado com uma CPU comum. [KASPERSKY, 2021]
Em uma aplicação web escrita em Python utilizando o framework Django, os ataques de Força Bruta podem ser evitados utilizando a biblioteca DjBrut. Diversas formas de verificação são realizadas para a segurança, entre elas estão limites de requisições de login por IP, login por usuário e frequência de requisições. [GITHUB, 2018]
Uma característica importante do DjBrut é a integração das configurações com o arquivo Settings.py, o qual faz parte da estrutura do Django e armazena as configurações do website, como, idioma, aplicações instaladas e localização. Ao final do arquivo Settings.py, os parâmetros do Djbrut devem ser adicionados conforme mostrado abaixo. [GITHUB, 2018]

```python
 from djbrut import Rule

 BRUTEFORCE_TIMELIMIT = 1  
 BRUTEFORCE_LIMITS = {
     'default': Rule(
         user=10,
         ip=10,
         csrf=10,
         freq=10,
     ),
     'index': Rule(
         user=0,
         ip=5,
         csrf=0,
         freq=0,
     ),
 }
```
Além da proteção contra a execução do ataque de Força Bruta, uma segunda linha de defesa pode ser adicionada por meio da Autenticação em Dois Fatores. Caso o atacante consiga obter a senha do usuário, não terá o acesso direto aos dados sigilosos pois uma segunda forma de autenticação será requisitada. Um website desenvolvido utilizando Django é possível implementar uma segunda barreira de autenticação por meio do django-two-factor-auth. Através dessa biblioteca, após o login tradicional feito por usuário e senha ser realizado, um segundo código é enviado ao usuário via mensagem de texto (SMS) ou criado por um aplicativo de celular destinado a gerar códigos temporários (OTP). Esse código será solicitado na segunda etapa de autenticação para somete depois disponibilizar o acesso à conta. [Django Two-Factor Authentication, 2021]
​
### 6. Sensitive Data Exposure
Informações sensíveis, como senhas, dados bancários, registros médicos e dados pessoais podem ser roubadas por atacantes quando armazenadas ou transmitidos em texto aberto ou com o uso de algoritmos de criptografia fracos. [OWASP,2017]
A exposição de dados sensíveis, além de prejuízos financeiros, pode causar danos à reputação das empresas que sofrerem vazamento dos dados que estavam desprotegidos. Também, penalidades descritas em legislações de países a respeito do tema podem ser aplicadas causando ainda mais danos financeiros. [BACH-NUTMAN, 2020]
A seguir serão apresentadas duas maneiras de exploração.

### 6.1. Sequestro de Sessão (Cookie)
O atacante consegue acesso indevido a informações após sequestrar a sessão legitima de um usuário. Quando o usuário realiza a autenticação no website é criado um controle de sessão HTTP por meio de cookies para manter o usuário autenticado. Esses cookies ficam armazenados no computador da vítima e podem ser roubados pelo atacante ou a informação que trafega entre o usuário e servidor pode ser interceptada e dados da autenticação acabarem sendo roubados. NAGPAL,2014]
Uma maneira eficaz de se proteger contra esse tipo de ameaça é o uso de criptografia no tráfego de dados. O uso de SSL ou TLS no protocolo HTTPS protege as informações que mantém a sessão ativa durante o tráfego, dificultando a obtenção de dados caso um atacante intercepte a conexão. [EC-Council, 2021]
Um website desenvolvido em Python pode proteger os dados trafegados por meio do framework Django. Por meio deste, os protocolos seguros SSL e TLS em HTTPS podem ser implementados na comunicação entre cliente e servidor, dificultando o sequestro da sessão. [DJANGO,2021]

### 6.2. Quebra de Hash de senhas
Um ataque de injeção SQL em um banco de dados ou alguma vulnerabilidade em um website, pode dar acesso ao arquivo de senhas dos usuários. Caso o arquivo esteja com as informações em texto aberto ou codificado com um algoritmo de hash que não seja forte o suficiente, as senhas facilmente podem ser vazadas ou utilizadas para aplicação de fraudes e acessos indevidos. [OWASP,2017]
Uma ferramenta largamente usada para quebras de hash é o HashCat, o qual, tem suporte para atacar mais de 300 tipos diferentes de algoritmos de hashing. Ainda, oferece suporte para GPU, desse modo, o ataque de recuperação das senhas pode ser acelerado. [HASHCAT, 2021]
Em Python, existe a biblioteca hashlib com suporte a diversos algoritmos de hash, entre eles o SHA3 e Blake2. Além do uso de algoritmos reconhecidos, uma política de criação de senhas complexas e longas por parte dos usuários reforça a segurança dificultando a quebra das senhas via força bruta.
A biblioteca hashlib é mostrada abaixo implementando o algoritmo SHA3.

```python
import hashlib

str = "String_senha" #Senha em texto aberto

hash_sha3_512 = hashlib.new("sha3_512", str.encode()) #Algoritimo de Hash selecionado e executado

print(hash_sha3_512)
print(hash_sha3_512.hexdigest())#Hash gerada
```
Em caso de dados sensíveis um algoritmo mais robusto e com maior resistência a ataques de força bruta pode ser utilizado. Um desses algoritmos de hash é o Argon2, um destaque desse método é a resistência a ataques oriundos de GPU. Em Python existe o suporte de algoritmo Argon2 por meio da biblioteca argon2. [ARGON2-CFFI, 2021]
Por padrão o Django utiliza o algoritmo PBKDF2 com hashes SHA256,  recomendado pelo NIST [DJANGO, 2021]. Porém o suporte ao Argon2 pode ser facilmente ajustado nos arquivos de configuração do Django

```python
 PASSWORD_HASHERS = [
 'django.contrib.auth.hashers.Argon2PasswordHasher',
 'django.contrib.auth.hashers.PBKDF2PasswordHasher',
 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
 'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
 ]

 from argon2 import PasswordHasher
 hasher = PasswordHasher()
 hash = hasher.hash("String_senha")
 hasher.verify(hash, "String_senha")
 hasher.verify(hash, "String_errada")
```
​
### 7. XSS (Cross-Site Scripting)
Segundo [PAULI 2014] XSS É uma das vulnerabilidades mais empregadas em plataformas web. Já [GROSMAN, HANSEN et al. 2007] destacam a presença deste tipo de vulnerabilidade desde meados de 1996 quando a Internet e os e-commerces começavam a se popularizar. Durante muitos anos figurou entre os 3 principais tipos de ataque web nas listas divulgadas pela OWASP. Na edição vigente, distribuída em 2017 percebe-se que sua incidência tem diminuído, provavelmente pela modernização dos frameworks de desenvolvimento e aprimoramento dos navegadores, visto que é uma vulnerabilidade explorada para execução de códigos Javascript no lado cliente.
Como genericamente os navegadores possuem suporte ao Javascript, muito utilizado para enriquecer o potencial e a usabilidade das interfaces de aplicações web, uma falha no tratamento de informações que serão exibidas na interface do usuário pode causar um abuso por parte do atacante, que tentará inserir trechos de Javascript que serão interpretados pelo navegador. 
Em um primeiro momento, a execução de Javascript no navegador pode parecer uma trivialidade e algo que independe de controles no lado servidor. Porém, existe um potencial danoso muitas vezes desconsiderado neste tipo de ataque. Mesmo que este ataque não seja executado no servidor, ele pode ser explorado para induzir o usuário a realizar ações indesejadas na aplicação, causar o vazamento de dados de controle de uma sessão autenticada permitindo seu sequestro, redirecionamento para páginas maliciosas etc. Conforme demonstra [WEIDMAN 2014], ataques XSS podem ser divididos em duas categorias: armazenados (stored) e refletidos (reflected). 
Nos ataques de XSS armazenados, o atacante se valerá da possibilidade de armazenar o vetor de ataque, que pode ser um trecho de código Javascript ou uma referência a um arquivo de extensão ".js" armazenado em um domínio web externo, entre dados que serão recuperados e exibidos para um usuário que será a vítima. Já nos ataques refletidos, será necessário induzir o usuário a enviar uma solicitação com o trecho de código malicioso, assim é provável que a vítima do ataque seja ludibriada por um phishing ou outro tipo de componente de engenharia social.
Os principais conjuntos de ferramentas de pentesting e scanners de vulnerabilidades possuem componentes eficientes para detectar pontos vulneráveis ao ataque XSS, favorecendo ferramentas especializadas em pentest do lado cliente (navegador) como o caso do BeEF (The Browser Exploitation Framework). 
Novamente a validação e tratamento dos dados de entrada na requisição web, bem como o tratamento dos dados que serão exibidos na interface com o usuário são os pontos de atenção para inibir este tipo de vulnerabilidade ou mitigar um ataque XSS.
Observa-se no trecho de código hipotético que tem por função realizar uma consulta e exibirá os resultados para um parâmetro informado: 
```python
template_vulneravel= '''
 <div ><p>Resultados para {}:</p></div>
 <div> {} </div>
 '''
 
 def vulnuravel():
     param = ""
     if request.method == 'POST' and 'param' in request.form.keys():
         param = request.form['parametro']
         dados = pesquisar_parametro(parametro)
     return template_vulneravel.format(parametro, dados)
```
Nesta situação, um código inserido num formulário de envio no campo "parametro" que servirá para consulta e será exibido em forma de título sem tratamento, torna-se um ponto vulnerável, permitindo a inserção de códigos maliciosos como nesta prova de conceito:

```html
<script>alert(document.cookie);</script>
```
Frameworks Python como o Django, amplamente empregados no desenvolvimento de aplicações web já incorporam tratamentos contra este tipo de situação em seus componentes de geração de formulários, funções de tratamento de parâmetros recebidos e exibição de variáveis em suas bibliotecas para templates. Como no exemplo semelhante
```python
def pesquisa(request):
    try:
        parametro = request.POST['parametro']
        dados = pesquisar_parametro(parametro)
        contexto = {'param': param, 'dados':dados}
    except KeyError:
        contexto = {'param': '', 'dados': ''}
    return render(request, 'exemplo/pesquisa.html', contexto)
```
Mesmo que o desenvolvedor não realize o tratamento do parâmetro recebido, sendo o parâmetro repassado diretamente ao template "pesquisa.html" para exibição:
```html
 <div><p>Resultados para {{param}}:</p></div>
   <div>{{dados}}</div>
```
As bibliotecas do Django envolvidas no processo automaticamente converterão trecho de código para entidades HTML, sanitizando os dados a serem exibidos:
```html
 <div><p>Resultados para: 
  &lt;script&gt;alert(document.cookie)&lt;/script&gt;:</p></div>
```
​
### Conclusão
Durante o processo de desenvolvimento de um software a segurança deve ser considerada de forma abrangente, iniciando ainda durante a etapa de levantamento de requisitos e continuando até os estágios finais de descontinuação da aplicação. Essa preocupação se deve a crescente quantidade de ameaças e a facilidade que invasores possuem de obter informações sobre novas vulnerabilidades e dados sensíveis que se sofrem exposição, somados ao crescente potencial computacional.

A segurança de aplicações web deve abranger todas as interfaces do software, desde a autenticação do usuário no frontend até a segurança dos dados armazenados em backend. Uma maneira de manter a aplicação atualizada nos requisitos de segurança e das boas práticas de segurança são as indicações de organizações como a OWASP.

Nesse trabalho foram abordadas algumas das vulnerabilidades do modelo OWASP de 2017 com o enfoque na linguagem Python. Para futuros trabalhos, pretende-se um estudo de todas as dez vulnerabilidades listadas na OWASP com o enfoque em Python e comparativos com outras linguagens de programação populares para web.

Os códigos utilizados neste artigo foram organizados neste repositório, originalmente  disponível em <https://github.com/zeandrade/tcc_pos_pucpr2019>. Neste mesmo repositório foram disponibilizados vídeos demostrativos das principais vulnerabilidades exploradas neste trabalho, bem como propostas de correções as mesmas, organizados no diretório “videos_demonstrativos”.
​
### Referências
Howard, M. e LIpner, S. (2006) “The security development lifecycle: SDL, a process for       developing demonstrably more secure software”. Microsoft Press, p.33-37. (Microsoft Press Series).

OWASP Top Ten. “OWASP Top 10 - 2017”. Disponível em: < https://owasp.org/www-pdf-archive/OWASP_Top_10-2017_%28en%29.pdf.pdf >. Acesso em 23/02/2021

Tiobe. “TIOBE Index for February 2021”. Disponível em: <https://www.tiobe.com/tiobe-index/>. Acesso em 23/02/2021

Borges, L. (2010) “Python para Desenvolvedores”. Novatec, p. 13-17.

Silva, I. e Silva, R. (2019) “LINGUAGEM DE PROGRAMAÇÃO PYTHON.” Revista Tecnologias em Projeção, v10, n°1, ano 2019.

Hattingh, C. (2016) “20 Python Libraries You Aren’t Using (But Should).” O’Reilly, p 2 - 3. 

Mozilla, “Introdução ao Django.” Disponível em: <https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Introduction>. Acesso em 27/02/2021

Menezes, N. (2019) “Introdução à programação com Python.” Novatec, p. 26 - 28.

Azzopardi, L. e David, M. (2016) “How to Tango with Django.” Leanpub, p.98.

Carvalho, A. (2014) “Segurança de aplicações web e os dez anos do relatório OWASP Top Ten: o que mudou ?”. Fasci-Tech – Periódico Eletrônico da FATEC-São Caetano do Sul, São Caetano do Sul, v.1, n. 8, Mar./Set. 2014

Hassan, M. M. et al. (2016) “Broken Authentication and Session Management Vulnerability: A Case Study Of Web Application.” DOI 10.5013/IJSSST, 2016
Pauli, J. (2014) “Introdução ao Web Hacking” Syngress/Novatec, p. 115-145.

Weidman, G. (2014) “Testes de Invasão” Novatec, p. 401-407.

Grossman,J. et al.(2007) “XSS Attacks” Syngress, Chapter 1.

Kohnfelder, Heymann et al. (2018) “Software Security Course” Disponível em: <https://research.cs.wisc.edu/mist/SoftwareSecurityCourse/>. Acesso em 05/03/2021

Nagpal, B. e et al (2014) “Preventive Measures for Securing Web Applications Using Broken Authentication and Session Management Attacks: A Study.” International Conference on Advances in Computer Engineering & Applications (ICACEA-2014) at IMSEC, GZB

Github. “DjBrut.” Disponível em: <https://github.com/orsinium-archive/django-bruteforce-protection> Acesso em 13/03/2021

EC-COUNCIL. “WHAT IS SESSION HIJACKING AND HOW TO PREVENT IT ?” Disponível em: <https://blog.eccouncil.org/what-is-session-hijacking-and-how-to-prevent-it/> Acesso em: 13/03/2021

 Django. “Security in Django.” Disponível em: <https://docs.djangoproject.com/en/3.1/topics/security/>. Acesso: 13/03/2021

Kaspersky. “O que é um ataque de força bruta ?” Disponível em: <https://www.kaspersky.com.br/resource-center/definitions/brute-force-attack>. Acesso em: 15/03/2021

Django Two-Factor Authentication.  “Django Two-Factor Authentication Documentation.” Disponível em: <https://django-two-factor-auth.readthedocs.io/en/stable/>. Acesso em: 15/03/2021

Bach-nutman. (2020) “Understanding The Top 10 OWASP Vulnerabilities.” Bournemouth University, 2020.

Hashcat. “Hashcat.” Disponível em: < https://hashcat.net/hashcat/>. Acesso em: 16/03/2021

Pypi. “pysha3.” Disponível em: <https://pypi.org/project/pysha3/> Acesso em:23/03/2021.

ARGON2-CFFI. “API Reference.” Disponível em: <https://argon2-cffi.readthedocs.io/en/stable/api.html> Acesso em:23/03/2021.

ENISA. “ENISA Threat Landscape - The year in review” Disponível em: < https://www.enisa.europa.eu/publications/year-in-review> Acesso em: 07/05/2021.

COMPUTERWORLD. “Déficit de profissionais de cibersegurança deve chegar a 3,5 milhões em 2021” Disponível em: < https://computerworld.com.br/seguranca/deficit-de-profissionais-de-ciberseguranca-deve-chegar-35-milhoes-em-2021/> Acesso em: 07/05/2021.
