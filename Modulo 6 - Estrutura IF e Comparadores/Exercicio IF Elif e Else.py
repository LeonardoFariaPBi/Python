meta = 10000
qntd_vendas = 10300

if qntd_vendas > meta:
    bonus = 0.03 * qntd_vendas
    print('Bonus de {}'.format(bonus))
elif qntd_vendas > (meta * 2):
    bonus = 0.09 * qntd_vendas
    print('Bonus de {}'.format(bonus))
else:
    print('Nao batemos a meta de vendas de Iphone, vendemos apenas {} unidades'.format(qntd_vendas))

meta = 10000
qntd_vendas = 10300

if qntd_vendas < meta:
    print('Nao batemos a meta de vendas de Iphone, vendemos apenas {} unidades'.format(qntd_vendas))
elif qntd_vendas > (meta * 2):
    bonus = 0.09 * qntd_vendas
    print('Bonus de {}'.format(bonus))
else:
    bonus = 0.03 * qntd_vendas
    print('Bonus de {}'.format(bonus))