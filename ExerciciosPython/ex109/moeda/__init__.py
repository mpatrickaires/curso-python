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
