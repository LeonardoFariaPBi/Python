#!/usr/bin/env python
# coding: utf-8

# # Exercícios Python

# ### Sua empresa resolveu pagar uma bonificação de R$1.000 para todos os funcionários com mais de 20 anos de casa. Quanto vai custar a ação de bonificação para a sua empresa?

# In[ ]:


anos_casa_funcionarios = [10, 15, 20, 25, 30, 47, 2, 5, 5, 6, 18, 32, 10, 1, 1, 2, 3, 3, 2, 1, 10, 40, 21, 10, 1, 2, 5, 7, 7, 6, 9, 19]

qtde_funcionarios_bonus = 0
premio = 1000

for tempo in anos_casa_funcionarios:
    if tempo >= 20:
        qtde_funcionarios_bonus += 1
        
print("Bonificação total", qtde_funcionarios_bonus * premio)    


# ### Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota
# 

# In[ ]:


notas = []
for i in range(4):
    nota = float(input("Digite a nota:"))
    notas.append(nota)

print("Média:", sum(notas) / len(notas))
print("Maior Nota:", max(notas))
print("Menor Nota:", min(notas))


# ### Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média (nova média = (antiga média + prova final) / 2). Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"

# In[ ]:


notas = []
print("Insira as 4 notas do período")
for i in range(4):
    nota = float(input("Digite a nota:"))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Media", media)
if media >= 7:
    print("APROVADO")
else:
    nota_prova_final = float(input("Nota Prova Final:"))
    media = (media + nota_prova_final) / 2
    print("Media depois da final", media)
    if media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")


# ### Desenvolva um programa que pergunte para o usuário o nome completo, cpf, endereço e duração do contrato e personalize todo o texto do contrato de acordo com as informações dadas.
# 

# In[ ]:


texto_contrato = """
CONTRATO DE PRESTAÇÃO DE SERVIÇOS PROFISSIONAIS

		Pelo presente instrumento particular de Contrato de Prestação de Serviços Contábeis, de um lado NOME_CONTRATANTE inscrita no CPF, sob nº CPF_CONTRATANTE,doravante denominada CONTRATANTE, residente e domiciliado(a)  à RUA_CONTRATANTE, Cidade CIDADE_CONTRATANTE, Estado ESTADO_CONTRATANTE, e o Contabilista Fulano, com escritório à Qualquer Lugar, Cidade Rio de Janeiro Estado RJ , inscrito no CNPJ Nº 22222222000100, doravante CONTRATADO(A), mediante as cláusulas e condições seguintes, tem justo e “Contratado” o que se segue:

CLAUSULA PRIMEIRA - A contratante neste ato, contrata os serviços profissionais do contratado(a) nas seguintes àreas:
		
1. Escrituração Contábil.
1.1 - Classificação da contabilidade de acordo com  normas e princípios contábeis vigentes;
1.2 - Emissão de Balancetes:
1.3 - Elaboração de Balanço anual e Demonstrativo de Resultado.
		
E por estarem de comum acordo, assinam o presente instrumento em duas vias, de igual teor e forma, na presença das testemunhas abaixo.


DIA_DATA/MES_DATA/ANO_DATA.


_________________________________                      __________________________
    Contratante - NOME_CONTRATANTE                                     Contratado(a)


"""


# In[ ]:


nome_contratante = input("Nome Contratante")
cpf_contratante = input("CPF Contratante")
rua_contratante = input("Rua e número do endereço do contratante")
cidade_contratante = input("Cidade Contratante")
estado_contratante = input("Estado Contratante")
data_contrato = input("Data no Formato DD/MM/AAAA")

dia_contrato = data_contrato[:2]
mes_contrato = data_contrato[3:5]
ano_contrato = data_contrato[6:]

texto_contrato = texto_contrato.replace("NOME_CONTRATANTE", nome_contratante)
texto_contrato = texto_contrato.replace("CPF_CONTRATANTE", cpf_contratante)
texto_contrato = texto_contrato.replace("RUA_CONTRATANTE", rua_contratante)
texto_contrato = texto_contrato.replace("CIDADE_CONTRATANTE", cidade_contratante)
texto_contrato = texto_contrato.replace("ESTADO_CONTRATANTE", estado_contratante)
texto_contrato = texto_contrato.replace("DIA_DATA", dia_contrato)
texto_contrato = texto_contrato.replace("MES_DATA", mes_contrato)
texto_contrato = texto_contrato.replace("ANO_DATA", ano_contrato)

print(texto_contrato)


# ### Crie um programa que converta a temperatura de celsius para Faremheit
#     - Agora adapte o programa para ele funcionar para uma lista de temperaturas
#     - Agora adapte o programa para ele conseguir fazer a conversão tanto de C para F quanto de F para C de acordo com a escolha do usuário.

# In[ ]:


# Parte 1

def conversor(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temperatura = float(input("Insira a temperatura em ºF"))
temperatura_celsius = conversor(temperatura)
print(f"{temperatura} ºF")
print("Temperatura em ºC", temperatura_celsius)


# In[ ]:


# Parte 2
while True:
    temperatura = input("Insira a temperatura em ºF, deixe em branco para pausar")
    if temperatura == "":
        break
    temperatura = float(temperatura)
    temperatura_celsius = conversor(temperatura)
    print(f"Temperatura em ºF: {temperatura} Temperatura em ºC: {temperatura_celsius}")


# In[ ]:


# Parte 3
def conversor(temperatura, escolha):
    if escolha == "F":
        celsius = (temperatura - 32) * 5 / 9
        return celsius
    else:
        fahrenheit = temperatura * 9 / 5 + 32
        return fahrenheit

escolha = input("Deseja inserir as temperaturas em ºC (digite C) ou ºF (digite F)")
if escolha == "C":
    medida_final = "F"
else:
    medida_final = "C"

while True:
    temperatura = input("Insira a temperatura em ºF, deixe em branco para pausar")
    if temperatura == "":
        break
    temperatura = float(temperatura)
    temperatura_convertida = conversor(temperatura, escolha)
    print(f"Temperatura em º{escolha}: {temperatura} Temperatura em º{medida_final}: {temperatura_convertida}")


# ### Analisador de Telefone
# 
# - Crie um programa que receba um telefone e verifique se ele é um telefone real brasileiro. Seu programa deve conseguir tratar espaços em branco, parênteses, existência de um 9º dígito no número ou não, existência de DDD ou não e deve obrigar o usuário a inserir o código do País (+55)
# 
# Válidos:<br>
# "+55 21 9799999999"<br>
# "+55 21 799999999 "<br>
# "+55 (21)79999-9999"<br>
# "+5521799999999"<br>

# In[ ]:


telefone = input("Insira seu telefone no formato +55XX999999999")

telefone = telefone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
if telefone[:3]!="+55":
    print("Esse telefone não é brasileiro ou foi inserido no formato errado")
else:
    if len(telefone)!=13 and len(telefone)!=14:
        print("Esse telefone não é brasileiro ou foi inserido no formato errado")
    else:
        print("Telefone válido:", telefone)


# ### Analisador de URL
#     - Seu programa deve pedir um link/URL para o usuário, como por exemplo: https://www.hashtagtreinamentos.com/blog
#     - Ele deve analisar essa URL dizendo:
#         - Domínio: hashtagtreinamentos.com
#         - Protocolo: HTTPS (tudo que vem antes de começar o endereço da URL, no caso antes do :)
#         - Caminho: /blog (tudo que vem depois do domínio, a partir da primeira / até antes dos parâmetros de busca)
#         - Parâmetros de busca: (Tudo que vem depois do ? e são separados entre si por um &. Os links podem ter isso ou não)
# 
# Exemplos de URL:
# 
# https://www.hashtagtreinamentos.com/blog<br>
# https://lp.hashtagtreinamentos.com/inscricao-intensivao-de-python-igfb?origemurl=curso&fonte=portal<br>
# https://lp.hashtagtreinamentos.com/inscricao-intensivao-de-python-igfb?origemurl=exercicios

# In[ ]:


url_analise = input("Insira uma URL")

posicao_doispoints = url_analise.find(":")
posicao_ponto = url_analise.find(".")
posicao_barrafimdominio = url_analise.find("/", posicao_ponto)
posicao_interrogacao = url_analise.find("?")

protocolo = url_analise[:posicao_doispoints]
print("Protocolo", protocolo)

dominio = url_analise[posicao_ponto+1:posicao_barrafimdominio]
print("Domínio", dominio)

caminho = url_analise[posicao_barrafimdominio:posicao_interrogacao]
print("Caminho", caminho)

texto_parametros_url = url_analise[posicao_interrogacao+1:]
parametros_url = texto_parametros_url.split("&")
print("Parâmetros URL", parametros_url)


# ### Crie um programa que dado o e-mail de um usuário, valide se aquele e-mail é válido com as seguintes regras:
#     - Tem que ter .com ou .gov
#     - Tem que ter @
#     - Tem que ter mais de 5 caracteres
#     - Não pode ter espaço

# In[ ]:


email = input("Insira o e-mail aqui:")

if ".com" in email or ".gov" in email:
    if "@" in email and len(email) > 5 and " " not in email:
        print("Email Válido")
    else:
        print("Email Inválido")
else:
        print("Email Inválido")


# ### ToDo List no Terminal
# 
# Crie um programa para criar uma lista de tarefas para o usuário (mais futuramente no curso, aprenderemos a armazenar essas informações em um banco de dados para essa lista poder ser editada e armazenada)
# 
# Seu programa deve pedir as tarefas que o usuário tem que fazer em um dia e, a cada inserção de uma nova tarefa, dizer que a tarefa foi adicionada a lista de tarefas. Quando o usuário digitar apenas enter no seu input (sem inserir nenhuma tarefa, seu programa deve printar a quantidade de tarefas para o dia e a lista de tarefas completa)

# In[ ]:


lista_tarefas = []

while True:
    tarefa = input("Escreva uma tarefa para adicionar a sua ToDo List")
    if tarefa == "":
        break
    else:
        lista_tarefas.append(tarefa)
        print(f"Tarefa adicionada com sucesso: {tarefa}")

print("Quantidade de tarefas para hoje:", len(lista_tarefas))
texto_tarefas = "\n".join(lista_tarefas)
print("Tarefas")
print(texto_tarefas)


# ### Conversor de Moedas
# 
# - Parte 1: Crie um conversor de moedas que pergunte para o usuário qual moeda ele quer converter e para qual moeda destino ele quer converter. Caso alguma das moedas não estejam na lista de conversão, o usuário deve ser informado que essa conversão não é possível. Sendo possível a conversão, o seu conversor de moedas deve em seguida pedir o valor da moeda de origem que ele quer converter para a moeda de destino, fazer a conversão e exibir para o usuário o valor convertido.
# - Parte 2: Adapte o seu código (crie uma cópia para manter os 2 códigos prontos) para o usuário não precisar dizer qual a moeda original, mas que permita inserir um valor para fazer a conversão com o indicativo da moeda, ex: R$50, US$20 e o sistema fazer a conversão automaticamente.

# In[ ]:


dic_conversoes = {
    "R$-US$": 0.194,
    "US$-R$": 5.15,
    "R$-BTC":  0.000002857,
    "BTC-R$": 350000,
    "BTC-US$": 67961.16,
    "US$-BTC": 0.000014714
}


# In[ ]:


# Parte 1
moedas = []
for par_moeda in dic_conversoes.keys():
    moeda_origem, moeda_destino = par_moeda.split("-")
    if moeda_origem not in moedas:
        moedas.append(moeda_origem)
texto_moedas = ",".join(moedas)
moeda_origem_usuario = input(f"Qual a moeda de origem para a conversão? ({texto_moedas})")

if moeda_origem_usuario in moedas:
    moeda_destino_usuario = input(f"Qual a moeda destino para a conversão? ({texto_moedas})")
    if moeda_destino_usuario not in moedas:
        print("Moeda inválida")
    else:
        if moeda_destino_usuario == moeda_origem_usuario:
            conversao = 1
        else:
            chave_dic = f"{moeda_origem_usuario}-{moeda_destino_usuario}"
            conversao = dic_conversoes[chave_dic]
        print(f"Conversão: {moeda_origem_usuario}1 = {moeda_destino_usuario}{conversao}")
else:
    print("Moeda inválida")


# In[ ]:


# Parte 2
moedas = []
for par_moeda in dic_conversoes.keys():
    moeda_origem, moeda_destino = par_moeda.split("-")
    if moeda_origem not in moedas:
        moedas.append(moeda_origem)
texto_moedas = ",".join(moedas)

valor_original = input("Insira o valor a converter")

moeda_origem_usuario = ""
for moeda in moedas:
    if moeda in valor_original:
        moeda_origem_usuario = moeda
        valor = float(valor_original.replace(moeda, ""))

if moeda_origem_usuario != "":
    moeda_destino_usuario = input(f"Qual a moeda destino para a conversão? ({texto_moedas})")
    if moeda_destino_usuario not in moedas:
        print("Moeda inválida")
    else:
        if moeda_destino_usuario == moeda_origem_usuario:
            conversao = 1
        else:
            chave_dic = f"{moeda_origem_usuario}-{moeda_destino_usuario}"
            conversao = dic_conversoes[chave_dic]
        valor_convertido = valor * conversao
        print(f"Conversão: {moeda_origem_usuario}{valor} = {moeda_destino_usuario}{valor_convertido}")
else:
    print("Moeda inválida")


# ### Você está analisando a conta de energia de um pequeno escritório e precisa saber:
# 1. Qual o valor total da conta de energia em cada mês do ano
# 2. Qual o valor total da conta de energia no ano
# 
# Considere as listas dadas como os 12 meses do ano, tanto para bandeiras quanto para consumo. O valor da conta é dado por: consumo * multiplicador_bandeira * preco_kwh

# In[1]:


bandeiras_tarifarias = ["vermelha", "vermelha", "amarela", "amarela", "verde", "verde", "verde", "verde", "verde", "amarela", "amarela", "amarela"]
consumo_kwh = [400, 350, 325, 350, 200, 220, 250, 290, 360, 290, 300, 300]
preco_kwh = 1.3
multiplicador = {"vermelha": 2, "amarela": 1.3, "verde": 1}


# In[2]:


precos_meses = []
for i, bandeira in enumerate(bandeiras_tarifarias):
    preco = multiplicador[bandeira] * preco_kwh * consumo_kwh[i]
    precos_meses.append(preco)

print(precos_meses)
print("Total Ano:", sum(precos_meses))


# ### Você recebeu uma lista de alunos da Arroba Treinamentos e precisa descobrir quantos alunos e quais aluno estão devendo ainda algum pagamento do curso. O curso custa 2.000 reais e os pagamentos dos alunos são representados por uma lista de valores já pagos no dicionário de alunos
# 

# In[ ]:


pagamentos_alunos = {
    "André": [2000],
    "Fulano": [1000, 1000],
    "Ciclano": [500, 500],
    "Beltrano": [100], 
    "João": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    "Amanda": [200, 300, 250, 250, 500, 400, 100],
    "Lira": [1000],
    "Alon": [10]
}


# In[ ]:


preco_curso = 2000
qtde_alunos_devendo = 0
for aluno in pagamentos_alunos:
    total_pago = sum(pagamentos_alunos[aluno])
    if total_pago < preco_curso:
        print(aluno, "está devendo", preco_curso - total_pago, "reais")
        qtde_alunos_devendo += 1

print(qtde_alunos_devendo, "estão devendo algum valor")


# ### Password Checker
# - Pessa para o usuário um input com a senha e um input com a confirmação de senha (aprenderemos no módulo de criação de telas com Python a fazer isso em um sistema bonito, mas para esse exercício faremos com inputs isso)
# - Para validar a senha, verifique que:
#     - A senha e confirmação são iguais
#     - A senha possua mais de 8 caracteres
#     - A senha tenha letras e números

# In[ ]:


senha = input("Senha")
confirmacao_senha = input("Confirmação de Senha")

if senha != confirmacao_senha:
    print("Senha e Confirmação são diferentes")
else:
    if senha.isnumeric() or senha.isalpha():
        print("Sua senha precisa ter letras e números")
    else:
        if len(senha) < 8:
            print("Sua senha precisa ter pelo menos 8 caracteres")
        else:
            print("Senha salva com sucesso")


# ### Você precisa criar a lógica de um sistema de load balance/redirecionamento automático. Seu programa deve receber um input que representa quantas requisições um sistema vai receber. Para cada requisição, seu sistema deve decidir em qual destino atribuir a requisição, destino A, B ou C. A regra de distribuição é: a primeira requisição é atribuída ao destino A, a segunda ao B, a terceira ao C, a quarta ao A, a quinta ao B, a sexta ao C, a sétima ao A, a oitava ao B, a nona ao C… e assim vai até o total de requisições. Ao final do programa, você deve calcular quais requisições foram para cada destino e quantas são. Ex: se o sistema deveria receber 80 requisições, no final seu código tem q dizer: destino A recebeu 27 requisições, destino B recebeu 27 requisições e destino C recebeu 26 requisicoes e a lista de requisições de cada destino: listaA = [1, 4, 7, 10, 13...], listaB = [2, 5, 8, 11, 14, ...], listaC = [3, 6, 9, 12, 15, 18, 21, ...].
# 

# In[ ]:


qtde_requisicoes = int(input("Quantas requisições você quer testar?"))

listaA = []
listaB = []
listaC = []

for i in range(qtde_requisicoes):
    if i % 3 == 0:
        listaA.append(i)
    elif i % 3 == 1:
        listaB.append(i)
    else:
        listaC.append(i)

print(f"Destino A: {len(listaA)} requisições")
print(f"Destino B: {len(listaB)} requisições")
print(f"Destino C: {len(listaC)} requisições")

print(listaA)
print(listaB)
print(listaC)



# ### ChatBot de Recomendações de Viagens
# - Você trabalha em uma agência de viagens e precisa criar um chatbot para os seus clientes. Esse chatbot deve pedir para o usuario escolher um mês de viagem. Em seguida, seu chatbot deve perguntar para qual lugar o usuário deseja viajar. Caso o local escolhido pelo usuário esteja na lista de bons lugares para viajar naquele mês, o seu chatbot deve dizer que é um ótimo lugar para viajar nesse mês. Caso o local não esteja na lista de bons locais daquele mês, seu chatbot deve:
#     1. Dizer para ele quais lugares são bons para viajar nesse mês
#     2. Verificar no resto dos meses se o local que o usuário quer viajar está em algum outro mês. Se tiver, seu programa deve dizer para ele qual o melhor mês para viajar para o local desejado pelo cliente.

# In[ ]:


viagens_mensais = {
    "jan": ["Tailândia", "Brasil", "Antártica", "África do Sul", "Argentina"],
    "fev": ["Tailândia", "Brasil", "Argentina", "Uruguai", "África do Sul"],
    "mar": ["Brasil", "Marrocos", "EUA", "Egito", "Dubai"],
    "abr": ["Brasil", "Marrocos", "Egito", "Dubai", "Equador"],
    "mai": ["Brasil", "EUA", "Itália", "França", "Inglaterra"],
    "jun": ["Brasil", "Itália", "França", "Grécia", "Turquia"],
    "jul": ["Brasil", "Itália", "França", "Grécia", "Turquia"],
    "ago": ["Brasil", "Itália", "França", "Grécia", "Turquia"],
    "set": ["Brasil", "Croácia", "Grécia", "México", "Alemanha"],
    "out": ["Brasil", "Alemanha", "Japão", "Chile", "Indonésia"],
    "nov": ["Brasil", "México", "Costa Rica", "Barbados", "Colômbia"],
    "dez": ["Tailândia", "México", "Costa Rica", "Barbados", "Colômbia"]
}

mes_viagem = input("Qual mês deseja viajar? Digite apenas as 3 primeiras letras do mês")

lista_paises = viagens_mensais[mes_viagem]

lugar_viagem = input("Para qual lugar deseja viajar?")

if lugar_viagem in lista_paises:
    print(f"Excelente momento para viajar para {lugar_viagem}! Vamos marcar sua viagem?")
else:
    texto_lugares = ", ".join(lista_paises)
    print(f"Hmm, {mes_viagem} não é um mês muito bom para {lugar_viagem}. Recomendamos em {mes_viagem}: {texto_lugares}")
    meses_alternativos = []
    for mes in viagens_mensais:
        if lugar_viagem in viagens_mensais[mes]:
            meses_alternativos.append(mes)
    if len(meses_alternativos) > 0:
        texto_meses_alternativos = ", ".join(meses_alternativos)
        print(f"Para viajar para {lugar_viagem} recomendamos viajar em: {texto_meses_alternativos}")


# ### Password Manager com dicionário sendo o Banco de Dados
# 
# - Seu desafio é criar um gerenciador de senhas (usando um dicionário python como banco de dados, mais para frente no curso no modulo de banco de dados você será capaz de armazenar essas senhas em um banco de dados de forma definitiva e mais protegida)
#     - Seu programa deve perguntar para o usuário se ele quer cadastrar uma senha nova ou pegar uma senha existente. Independente da operação ele deve usar uma senha mestre: "uh&g7fnsd8" para aprovar qualquer consulta/edição no sistema. Se o usuário quiser adicionar uma senha, deve pedir qual o nome do sistema de onde essa senha faz parte, qual o login e qual a senha a ser cadastrada. Se for para consultar, seu programa deve exibir os nomes dos sistemas disponíveis e o usuário pode escolher qual senha quer pedir e seu programa deve dar para ela a resposta de login e senha. Se quiser que as suas senhas cadastradas possam ser usadas para consulta, coloque tudo em um loop infinito e dê algum comando para o usuário conseguir finalizar o processo

# In[ ]:


gerenciador_senhas = {
    "Gmail": ("lira@emailfalso.com", "minhasenha123"),
    "Github": ("pythonimpressionador", "senhadoida"),
    "Cartão de Crédito": ("NumeroFalsodoCartao", "123456"),
    "Portal Hashtag": ("usuario@gmail.com", "123456")
}

senha_banco = input("Digite a senha mestre para acessar o banco")
if senha_banco != "uh&g7fnsd8":
    print("Senha incorreta, acesso negado.")
else:
    acao = input("O que você deseja fazer? Cadastrar (digite 1) ou Consultar uma senha (digite 2). Deixe em branco para finalizar")
    while acao != "":
        if acao == "1":
            nome_sistema = input("Digite o nome do sistema a ser cadastrado")
            login = input("Digite o login")
            senha = input("Digite a senha")
            gerenciador_senhas[nome_sistema] = (login, senha)
            print(f"Senha salva com sucesso. {nome_sistema}: {gerenciador_senhas[nome_sistema]}")
        elif acao == "2":
            nomes_sistemas = list(gerenciador_senhas.keys())
            texto_nomes_sistemas = "\n".join(gerenciador_senhas)
            print("Sistemas disponíveis:")
            print(texto_nomes_sistemas)
            sistema = input("Escolha o sistema que quer consultar a senha. Digite o nome exatamente como aparece acima.")
            usuario, senha = gerenciador_senhas[sistema]
            print("Usuário {}".format(usuario))
            print("Senha {}".format(senha))
        else:
            break
        acao = input("O que você deseja fazer? Cadastrar (digite 1) ou Consultar uma senha (digite 2). Deixe em branco para finalizar")
        


# ### Extrator de data em email
# 
# - Crie um código que consiga extrair a data escrita em um email no formato DIA/MES/ANO. Essa data pode estar com diferentes quantidades de dígitos para cada informação de DIA/MES/ANO. Ex: 01/05/2024 = 1/5/24
# - Mais para frente no curso vamos aprender regex que facilita esse tipo de extração, por enquanto, para esse exercício pode considerar que apenas 1 data será incluída no email e que não será usado mais a / em outros locais do email

# In[ ]:


texto_email = """Prezados,
Segue em anexo contrato para aprovação e assinatura até o dia 10/12/2025
Favor se atentar ao prazo de conclusão para evitar o cancelamento do serviço.
Att.,
Fulano Beltrano"""


# In[ ]:


posicao_barra = texto_email.find("/")
posicao_barra2 = texto_email.find("/", posicao_barra+1)
dia = texto_email[posicao_barra-2:posicao_barra].strip()
mes = texto_email[posicao_barra+1:posicao_barra2]
ano = texto_email[posicao_barra2+1:posicao_barra2+5]

if "\n" in ano: # esses ifs é para tratar o que pode vir depois do ano, caso o ano tenha apenas 2 dígitos. Pode vir um ponto, pode vir um espaço, pode vir um enter. Independente do caso, só queremos aquilo antes desses separadores
    ano = ano.split("\n")[0]
if "." in ano:
    ano = ano.split(".")[0]
if " " in ano:
    ano = ano.split(" ")[0]

print("Dia", dia)
print("Mês", mes)
print("Ano", ano)


# ### Extrator de contato em email
# 
# - Crie um código que consiga extrair um endereço de e-mail de um texto.
# - Mais para frente no curso vamos aprender regex que facilita esse tipo de extração, por enquanto, para esse exercício pode considerar que apenas 1 email será incluída no texto e o @ não será usado em outros locais.

# In[ ]:


texto_email = """Prezados,
Favor encaminhar documentação para o email qualquercoisa@gmail.com
Obrigado"""


# In[ ]:


# Existem diferentes formas de fazer esse exercício, faremos considerando que o email sempre tem ou espaço ou quebra de linha antes ou depois dele, o que é bem provável
linhas = texto_email.split("\n")
for linha in linhas:
    if "@" in linha:
        palavras = linha.split(" ")
        for palavra in palavras:
            if "@" in palavra:
                email = palavra

print(email)


# ### Dado um dicionário com a temperatura em várias cidades, máximas e mínimas estimadas e máximas e mínimas reais, veja em quantas cidades a previsão do tempo acertou e em quantas errou.
# 
# Considere que a previsão erra se a mínima real for menor do que a mínima estimada OU se a máxima real for maior do que a máxima estimada. Se os valores reais estiverem dentro da faixa estimada, mesmo que os valores não sejam iguais, é considerado que a previsão acertou.
# 
# Ex: <br>
# Mínima Estimada: 20, Máxima Estimada: 25, Mínima Real: 21, Máxima Real: 25 -> acertou<br>
# Mínima Estimada: 20, Máxima Estimada: 25, Mínima Real: 19, Máxima Real: 25 -> errou<br>
# Mínima Estimada: 20, Máxima Estimada: 25, Mínima Real: 23, Máxima Real: 24 -> acertou<br>
# Mínima Estimada: 20, Máxima Estimada: 25, Mínima Real: 19, Máxima Real: 28 -> errou<br>
# 
# formato:
# (minima_estimada, maxima_estimada, minima_real, maxima_real)

# In[ ]:


dic_temperaturas = {
    "São Paulo": (15, 23, 16, 22),
    "Rio de Janeiro": (21, 25, 20, 25),
    "Belo Horizonte": (19, 22, 19, 22),
    "Brasília": (23, 25, 19, 21),
    "Porto Alegre": (13, 19, 14, 18),
    "Natal": (25, 28, 24, 28),
    "Salvador": (22, 29, 23, 30),
    "Manaus": (23, 27, 23, 26),
}


# In[ ]:


errou = 0
acertou = 0
for cidade in dic_temperaturas:
    min_estimada, max_estimada, min_real, max_real = dic_temperaturas[cidade]
    if min_real < min_estimada or max_real > max_estimada:
        errou += 1
    else:
        acertou += 1
print(f"Errou em {errou} cidades e acertou em {acertou} cidades")


# ### Você trabalha em uma montadora de veículos com 32 distribuidores e a meta da sua empresa era produzir e entregar 50.000 veículos no ano. Essa meta foi batida, com folga. Seu chefe então se questionou: se a gente tivesse 31 distribuidoras, ainda assim a gente teria batido a meta? E se a gente tivesse 30? E 29?
# 
# Seu objetivo então é descobrir qual o menor número de distribuidores que teria permitido a sua empresa a ter batido essa meta de 50.000 veiculos produzidos e entregues no ano.

# In[ ]:


entregas_distribuidores = [5000, 4000, 3900, 3900, 3800, 3200, 3000, 3000, 3000, 3000, 2950, 2950, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900, 2900]

soma_entregas = 0
meta = 50000

i = 0
while soma_entregas < meta:
    soma_entregas = soma_entregas + entregas_distribuidores[i]
    i = i + 1

print(i, "seria o menor número possível de distribuidores que permitira bater a meta de 50.000 veículos")


# ### Um dos princípios mais importantes nas empresas é o princípio 80/20. No geral, 20% das ações que uma empresa faz geram 80% dos resultados. Isso tanto para receita, quanto para custos, etc. Você está analisando uma empresa de bebidas. Tendo isso em mente, queremos descobrir quais as linhas de custos que representam 80% do total gasto da empresa. Para isso, calcule quanto percentualmente cada custo representa do custo total da empresa e crie um ranking decrescente baseado nesse percentual 

# In[ ]:


custos = [
    (10131.7, "Custo Mercadorias Vendidas"),
    (2916, "Logística"),
    (1741, "Despesas Comerciais"),
    (1305, "Despesas administrativas"),
    (28, "Outros Itens"),
    (997, "Juros e Resultado Financeiro"),
    (14, "Participações em outros Empreendimentos"),
    (58, "Impostos")
]


# In[ ]:


custos.sort(reverse=True)
total = sum(item[0] for item in custos)

percentual_acumulado = 0
for i in range(len(custos)):
    valor, descricao = custos[i]
    percentual_acumulado += (valor / total)
    custos[i] = (valor, descricao, valor / total, percentual_acumulado)

print(custos)


# ### Você trabalha em uma empresa que possui várias franquias. Queremos saber quais as franquias que têm maior número de funcionários e quais dessas, juntas, representam 80% dos funcionários da rede toda.

# In[ ]:


franquias = [
    (25000, "Loja A"),
    (10000, "Loja B"),
    (500, "Loja C"),
    (25000, "Loja D"),
    (1200, "Loja E"),
    (400, "Loja F"),
    (200, "Loja G"),
    (15, "Loja H"),
    (200, "Loja I"),
    (15, "Loja J"),
    (200, "Loja K"),
    (15, "Loja L"),
    (200, "Loja M"),
    (15, "Loja N"),
]


# In[ ]:


franquias.sort(reverse=True)
total_funcionarios = sum(item[0] for item in franquias)

percentual_acumulado = 0

for i in range(len(franquias)):
    qtde_funcionarios, descricao = franquias[i]
    percentual_acumulado += qtde_funcionarios / total_funcionarios
    franquias[i] = (qtde_funcionarios, descricao, qtde_funcionarios / total_funcionarios, percentual_acumulado)

print(franquias)


# ### Desafio (esse exercício é mais difícil mesmo)
# ### Com o PIB de 2022 e de 2021 de cada estado brasileiro, descubra: qual o maior PIB, menor PIB, média do PIB, PIB total em cada ano e qual estado mais cresceu o PIB percentualmente e em valores absolutos de um ano pro outro

# In[ ]:


pib_2022 = {
    "Acre": 21374,
    "Alagoas": 76266,
    "Amapá": 20100,
    "Amazonas": 131531,
    "Bahia": 352618,
    "Ceará": 194885,
    "Distrito Federal": 286944,
    "Espírito Santo": 186337,
    "Goiás": 269628,
    "Maranhão": 124981,
    "Mato Grosso": 233390,
    "Mato Grosso do Sul": 142204,
    "Minas Gerais": 857593,
    "Paraná": 549973,
    "Paraíba": 77470,
    "Pará": 262905,
    "Pernambuco": 220814,
    "Piauí": 64028,
    "Rio de Janeiro": 949301,
    "Rio Grande do Norte": 80181,
    "Rio Grande do Sul": 581284,
    "Rondônia": 58170,
    "Roraima": 18203,
    "Santa Catarina": 428571,
    "Sergipe": 51861,
    "São Paulo": 2719751,
    "Tocantins": 51781
}

pib_2021 = {
    "Acre": 16476,
    "Alagoas": 63202,
    "Amapá": 18469,
    "Amazonas": 116019,
    "Bahia": 305321,
    "Ceará": 166915,
    "Distrito Federal": 265847,
    "Espírito Santo": 138446,
    "Goiás": 224126,
    "Maranhão": 106916,
    "Mato Grosso": 178650,
    "Mato Grosso do Sul": 122628,
    "Minas Gerais": 682786, 
    "Paraná": 487931,
    "Paraíba": 70292,
    "Pará": 215936,
    "Pernambuco": 193307,
    "Piauí": 56391,
    "Rio de Janeiro": 753824,
    "Rio Grande do Norte": 71577,
    "Rio Grande do Sul": 470942, 
    "Rondônia": 51599,
    "Roraima": 16024,
    "Santa Catarina": 349275,
    "Sergipe": 45410,
    "São Paulo": 2377639,
    "Tocantins": 43650
    }


# In[ ]:


valores_pib21 = list(pib_2021.values())
estados_pib21 = list(pib_2021.keys())
valores_pib22 = list(pib_2022.values())
estados_pib22 = list(pib_2022.keys())


total_pib_2022 = sum(valores_pib22)
total_pib_2021 = sum(valores_pib21)
media_pib_2022 = total_pib_2022 / len(pib_2022)
media_pib_2021 = total_pib_2021 / len(pib_2021)
print("2022", "Total PIB:", total_pib_2022, "Média PIB:", media_pib_2022)
print("2021", "Total PIB:", total_pib_2021, "Média PIB:", media_pib_2021)


maior_pib2021 = max(valores_pib21)
menor_pib2021 = min(valores_pib21)
maior_pib2022 = max(valores_pib22)
menor_pib2022 = min(valores_pib22)

indice_maior_pib21 = valores_pib21.index(maior_pib2021)
estado_maiorpib2021 = estados_pib21[indice_maior_pib21]
print("Maior PIB de 2021:", maior_pib2021, "Estado:", estado_maiorpib2021)

indice_maior_pib22 = valores_pib22.index(maior_pib2022)
estado_maiorpib2022 = estados_pib22[indice_maior_pib22]
print("Maior PIB de 2022:", maior_pib2022, "Estado:", estado_maiorpib2022)

indice_menor_pib21 = valores_pib21.index(menor_pib2021)
estado_menorpib2021 = estados_pib21[indice_menor_pib21]
print("menor PIB de 2021:", menor_pib2021, "Estado:", estado_menorpib2021)

indice_menor_pib22 = valores_pib22.index(menor_pib2022)
estado_menorpib2022 = estados_pib22[indice_menor_pib22]
print("menor PIB de 2022:", menor_pib2022, "Estado:", estado_menorpib2022)

maior_alta_pib_perc = 0
estado_maioralta_pib_perc = ""
maior_alta_pib_abs = 0
estado_maioralta_pib_abs = ""
for estado in pib_2021:
    pib21_estado = pib_2021[estado]
    pib22_estado = pib_2022[estado]
    alta_abs = pib22_estado - pib21_estado
    percentual_alta = alta_abs / pib21_estado

    if alta_abs > maior_alta_pib_abs:
        maior_alta_pib_abs = alta_abs
        estado_maioralta_pib_abs = estado
    
    if percentual_alta > maior_alta_pib_perc:
        maior_alta_pib_perc = percentual_alta
        estado_maioralta_pib_perc = estado


print("Maior alta pib Percentual:", maior_alta_pib_perc, "Estado:", estado_maioralta_pib_perc)
print("Maior alta pib absoluto:", maior_alta_pib_abs, "Estado:", estado_maioralta_pib_abs)


# ### Desafio (esse exercício é mais difícil mesmo)
# ### Temos o preço de diferentes ações no início de 2024 e em maio de 2024, queremos:
#     - Ação que mais subiu, ação que mais caiu no período (percentualmente)
#     - Se tivessemos 1.000 reais investido em um portfólio com as ações da carteira A vs um portfólio com as ações B, qual teria rendido mais? - considere que os 1.000 reais são investidos de forma proporcional entre cada ativo da carteira

# In[ ]:


acoes = {
    "PETR4": [37.78, 37.01],
    "VALE3": [77.05, 65.30],
    "ITUB4": [33.52, 33.74],
    "ABEV3": [13.71, 11.81],
    "WEGE3": [36.57, 38.35],
    "BBAS3": [27.38, 29.41],
    "JBSS3": [25.17, 29.96],
    "SBSP3": [73.63, 75.07]
}

carteiraA = ["PETR4", "VALE3", "JBSS3", "SBSP3"]
carteiraB = ["WEGE3", "BBAS3", "ITUB4", "ABEV3"]


# In[ ]:


acao_mais_subiu = ""
percentual_mais_subiu = 0
acao_mais_caiu = ""
percentual_mais_caiu = 0

for acao in acoes:
    precos = acoes[acao]
    preco_inicio = precos[0]
    preco_fim = precos[1]
    variacao_percentual = preco_fim / preco_inicio - 1
    if variacao_percentual > percentual_mais_subiu:
        acao_mais_subiu = acao
        percentual_mais_subiu = variacao_percentual
    elif variacao_percentual < percentual_mais_caiu:
        acao_mais_caiu = acao
        percentual_mais_caiu = variacao_percentual

print(acao_mais_subiu, f"Subiu {percentual_mais_subiu}")
print(acao_mais_caiu, f"Caiu {percentual_mais_caiu}")


# In[ ]:


variacoes = {}

for acao in acoes:
    precos = acoes[acao]
    preco_inicio = precos[0]
    preco_fim = precos[1]
    variacao_percentual = preco_fim / preco_inicio - 1
    variacoes[acao] = variacao_percentual

print(variacoes)

valor_investido = 1000 / len(carteiraA)
valor_total_carteiraA = 0
valor_total_carteiraB = 0
for acao in carteiraA:
    valor_final_acao = variacoes[acao] * valor_investido + valor_investido
    valor_total_carteiraA += valor_final_acao
for acao in carteiraB:
    valor_final_acao = variacoes[acao] * valor_investido + valor_investido
    valor_total_carteiraB += valor_final_acao

print(valor_total_carteiraA)
print(valor_total_carteiraB)

