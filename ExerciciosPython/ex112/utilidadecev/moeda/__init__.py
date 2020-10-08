def metade(valor, cifrao=False):
    if cifrao:
        return moeda(valor / 2)
    else:
        return valor / 2


def dobro(valor, cifrao=False):
    if cifrao:
        return moeda(valor * 2)
    else:
        return valor * 2


def aumentar(valor, porcentagem, cifrao=False):
    if cifrao:
        return moeda(valor + (valor * (porcentagem / 100)))
    else:
        return valor + (valor * (porcentagem / 100))


def diminuir(valor, porcentagem, cifrao=False):
    if cifrao:
        return moeda(valor - (valor * (porcentagem / 100)))
    else:
        return valor - (valor * (porcentagem / 100))


def moeda(valor):
    return f'R${valor}'


def linha():
    print('-' * 30)


def resumo(valor, mais=0, menos=0):
    linha()
    print(f'{"RESUMO DO VALOR":^30}')
    linha()
    print(f'{"Preço analisado:":<20} R${valor:,.2f}')
    print(f'{"Dobro do preço:":<20} R${dobro(valor):.2f}')
    print(f'{"Metade do preço:":<20} R${metade(valor):.2f}')
    print(f'{f"{mais}% de aumento:":<20} R${aumentar(valor, mais):.2f}')
    print(f'{f"{menos}% de redução:":<20} R${diminuir(valor, menos):.2f}')
    linha()
