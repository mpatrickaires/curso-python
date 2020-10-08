def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma (total, maior nota, menor nota, média e
    situação (opcional)).
    """
    ficha = {'total': len(n),
             'maior': max(n),
             'menor': min(n),
             'média': sum(n) / len(n)}
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'BOA'
        elif ficha['média'] >= 5:
            ficha['situação'] = 'RAZOÁVEL'
        else:
            ficha['situação'] = 'RUIM'
    return ficha


# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4)
print(resp)
help(notas)
