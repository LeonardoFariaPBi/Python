meta = 50000
qntd_vendas = 65300

if qntd_vendas > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qntd_vendas))
else:
    print('Infelizmente nao batemos a meta, vendemos apenas {} unidades. A meta era de {} unidades'.format(qntd_vendas, meta))