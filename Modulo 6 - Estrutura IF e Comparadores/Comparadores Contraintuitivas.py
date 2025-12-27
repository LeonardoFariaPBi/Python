faturamento = input("Digite o faturamento da loja: ")
custo = input("Digite o custo da loja: ")

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de {}' .format(lucro))
else:
    print('Preencha o faturamento e o custo corretamente')