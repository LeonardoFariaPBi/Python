    # IF e AND
meta_func = 10000
meta_loja = 250000
qntd_vendas_func = 11000
qntd_vendas_loja = 900000

if qntd_vendas_func > meta_func and qntd_vendas_loja > meta_loja:
    bonus = 0.03 * (qntd_vendas_func + qntd_vendas_loja)
else:
    bonus = 0
    print('Bonus de {}'.format(bonus))

    # IF e OR
meta_func = 10000
meta_loja = 250000
qntd_vendas_func = 25000
qntd_vendas_loja = 280000

if qntd_vendas_func > meta_func or qntd_vendas_loja > meta_loja:
    bonus = 0.03 * (qntd_vendas_func + qntd_vendas_loja)
    print('Bonus de {}'.format(bonus))
else:
    bonus = 0
    print('Bonus de {}'.format(bonus))

# IF e (OR AND)
nota_funcionario = 9
meta_nota = 9
meta_func = 10000
meta_loja = 250000
qntd_vendas_func = 5000
qntd_vendas_loja = 280000

if nota_funcionario >= meta_nota or (meta_func and qntd_vendas_loja > meta_loja):
    bonus = 0.03 * qntd_vendas_func
    print('Bonus de {}'.format(bonus))
else:
    bonus = 0
    print('Bonus de {}'.format(bonus))