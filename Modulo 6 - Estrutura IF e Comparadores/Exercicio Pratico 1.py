# 1- IF com ELSE

vendas_func1 = 1000
vendas_func2 = 770
vendas_func3 = 2700

if vendas_func1 >= 1000:
    print("O funcionario 1 ganhou {} de bonus" .format(vendas_func1 * 0.1))

if vendas_func2 >= 1000:
    bonus = vendas_func2 * 0.1
else:
    bonus = 0
print("O funcionario 2 ganhou {} de bonus" .format(bonus))

if vendas_func3 >= 1000:
    bonus = vendas_func3 * 0.1
else:
    bonus = 0
print("O funcionario 3 ganhou {} de bonus" .format(bonus))

# 2- IF com ELIF

vendas_func1 = 1000
vendas_func2 = 770
vendas_func3 = 2700

if vendas_func2 >= 2000:
    bonus = vendas_func2 * 0.15
elif vendas_func2 >= 1000:
    bonus = vendas_func2 * 0.1
else:
    bonus = 0
    print("O funcionario 2 ganhou {} de bonus" .format(bonus))

# 3- IF ELIF e IF ELSE

vendas_func1 = 1000
vendas_func2 = 770
vendas_func3 = 2700

if vendas_func1 >= 1000:
    if vendas_func1 >= 2000:
        bonus = vendas_func1 * 0.15
    else:
        bonus = vendas_func1 * 0.1
else:
    bonus = 0
print("O funcionario 1 ganhou {} de bonus" .format(bonus))

if vendas_func3 >= 1000:
    if vendas_func3 >= 2000:
        bonus = vendas_func3 * 0.15
    else:
        bonus = vendas_func3 * 0.1
else:
    bonus = 0
print("O funcionario 3 ganhou {} de bonus" .format(bonus))