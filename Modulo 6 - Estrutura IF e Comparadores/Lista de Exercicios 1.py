# Exercicio 1: Verificação de estoque de produtos


# ENTRADA DE DADOS
try:
    cont_alimentos = int(input("Digite a quantidade de alimentos: "))
    cont_bebidas = int(input("Digite a quantidade de bebidas: "))
    cont_limpeza = int(input("Digite a quantidade de limpeza: "))
except ValueError:
    print("Erro: digite apenas números.")
    exit()

# ESTOQUE MÍNIMO
est_alimento_min = 50
est_bebida_min = 70
est_limpeza_min = 30

print("\n--- VERIFICAÇÃO DE ESTOQUE ---")

# ALIMENTOS
if cont_alimentos < est_alimento_min:
    print(f"Pegue mais alimentos, temos apenas {cont_alimentos} unidades.")
else:
    print(f"Estoque suficiente de alimentos: {cont_alimentos} unidades.")

# BEBIDAS
if cont_bebidas < est_bebida_min:
    print(f"Pegue mais bebidas, temos apenas {cont_bebidas} unidades.")
else:
    print(f"Estoque suficiente de bebidas: {cont_bebidas} unidades.")

# LIMPEZA
if cont_limpeza < est_limpeza_min:
    print(f"Pegue mais produtos de limpeza, temos apenas {cont_limpeza} unidades.")
else:
    print(f"Estoque suficiente de limpeza: {cont_limpeza} unidades.")

print("\nFim do programa")

# Exercicio 2: Verificação de presença de item em texto

texto = input("Digite uma FRASE ou TEXTO: ")
procurar = input("Digite o que voce quer procurar: ")

if procurar in texto:
    print("Achamos o seguinte item procurado: " + str(procurar))
else:
    print("Nao achamos o que vc procura!")