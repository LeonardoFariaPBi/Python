    # Lista de Estrutura Sequencial
    # 1. Faça um Programa que mostre a mensagem (print) \"Alo mundo\" na tela.
    # 2. Faça um Programa que peça um número (input) e então mostre a mensagem: \"O número informado foi [número].
    # 3. Faça um Programa que peça dois números e imprima a soma.
    # 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
    # 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).
    # 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.
    # 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
    # 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    # 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
    # 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
    # P = 72,7h - 58$
    # 11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # a. Para homens: $P = 72,7h - 58$",
    # b. Para mulheres: $P = 62,1h - 44,7$"
    # 12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês."
    # Calcule o salário bruto (horas * salario por hora)
    # Calcule o desconto do IR (11% do salário bruto)
    # Calcule o desconto do INSS (8% do salário bruto)
    # Calcule o desconto do sindicato (5% do salário bruto)
    # Calcule o salário líquido (salário bruto - descontos)
    # 13. Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#(para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas
#vamos trabalhar isso em breve
    # 14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).\n",
    # "Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. "


    # Primeiro DESAFIO, REGULARIZE A ESTRUTURA. LEMBRANDO FIZEMOS OS SEGUINTES EXERCICIOS: 1, 2, 3, 4, 5, 6, 7, 8 E 9.

# 1 - Exercicio

print("Alo, mundo")

# 2 - Exercicio

numero = input("Digite um numero: ")
print("O numero informado foi {}" .format(numero))

# 3 - Exercicio

numero1 = int(input("Digite um numero a ser somado: "))
numero2 = int(input("Digite um segundo numero a ser somado com o anterior: "))
soma = numero1 + numero2
print(soma)

# 4 - Exercicio

nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
nota3 = float(input('Informe a 3ª nota: '))
nota4 = float(input('Informe a 4ª nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('A média é:', media)

# 5 - Exercicio

comprimento_m = float(input('Informe um comprimento em metros: '))
comprimento_cm = comprimento_m * 100
print('Este comprimento em centímetros é:', comprimento_cm, 'cm')

# 6 - Exercicio

largura = float(input('Informe a largura da sala em metros: '))
comprimento = float(input('Informe o comprimento da sala em metros: '))
area = largura * comprimento
print('A área da sala é:', area, 'm²')

# 7 - Exercicio

valor_hora = float(input('Informe o valor ganho por hora em R$/h: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '))
total = valor_hora * horas_trabalhadas
print('O salário do mês foi: R$', total)

# 8 - Exercicio

temperatura_f = float(input('Informe a temperatura em Fahrenheit: '))
temperatura_c = (5/9) * (temperatura_f - 32)
print('A temperatura é:', temperatura_c, '°C')

# 9 - Exercicio

temperatura_c = float(input('Informe a temperatura em Celsius: '))
temperatura_f = 9/5 * temperatura_c + 32
print('A temperatura é:', temperatura_f, '°F')

# 10 - Exercicio
    
altura = float(input('Informe a altura em metros: '))
peso_ideal = 72.7 * altura - 58
print('O peso ideal é:', peso_ideal, 'kg')

# Exercicio 11

altura = float(input("Digite sua altura em metros. Ex: 1.70: "))
sexo_MF = int(input("Selecione = 1 - Masculino ou 2 - Feminino: "))
formula1M = 72.7
formula2M = 58
formula1F = 62.1
formula2F = 44.7
resultado = []

if sexo_MF == 1:
    resultado = formula1M * altura - formula2M    
    print(f"Peso ideal masculino: {resultado:.2f}")
elif sexo_MF == 2:
    resultado = formula1F * altura - formula2F    
    print(f"Peso ideal femino: {resultado:.2f}")
else:
    print("Tente novamente! Voce deve escolher 1 ou 2.")
    
# Exercicio 12

salario_hora = float(input("Digite quanto voce ganha por hora = Ex: 100.00 ou 65.29: "))
print(f"R${salario_hora:.2f}")
horas = int(input("Digite quantas horas trabalhou no mes: "))
print(f"Trabalhou: {horas} horas.")
salario_bruto = (horas * salario_hora)
print(f"R${salario_bruto:.2f}")

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
imposto = ir + inss + sindicato
salario_liquido = salario_bruto - inss

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR (11%): R$ {ir:.2f}")
print(f"Desconto INSS (8%): R$ {inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Exercicio 13

area = float(input("Digite a area em m², que sera pintada: "))
preco_lata = 80
litro_rendimento = 3

litros = (area / litro_rendimento ) / 18
latas = litros / 1
preco_total = latas * preco_lata
print(f"Voce precisara de {latas:.2f} latas de tinta com um custo total de {preco_total:.2f}")

# Exercicio 14

tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade da internet em Mbps: "))
tamanho_megabits = tamanho * 8
tempo = tamanho_megabits / velocidade
tempo_minutos = tempo / 60
print(f'O tempo de download é de {tempo_minutos} minutos')