meta_func = int(input("Digite a meta do funcionario: "))
meta_loja = int(input("Digite a meta da loja: "))
vendas_func = int(input("Digite a Qntd de vendas realizada pelo funcionario: "))
vendas_loja = int(input("Digite a Qntd de vendas da loja: "))

# Tipo 1
if vendas_func > meta_func and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_func
    print("Bonus de funcionario foi de {}" .format(bonus))
else:
    print("Funcionario nao ganhou bonus")
# Tipo 2    
if vendas_func > meta_func or vendas_loja > meta_loja:
    bonus = 0.03 * vendas_func
    print("Bonus de funcionario foi de {}" .format(bonus))
else:
    print("Funcionario nao ganhou bonus")
# Tipo 3    
if vendas_func < meta_func or vendas_loja < meta_loja:
    bonus = 0.03 * vendas_func
    print("Bonus de funcionario foi de {}" .format(bonus))
else:
    print("Funcionario nao ganhou bonus")