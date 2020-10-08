expressao = str(input('Digite a expressão: ')).strip()
listaExpressao = expressao
validacao = False
parenteseAbre = parenteseFecha = 0

if listaExpressao.count('(') == listaExpressao.count(')'):
    validacao = True

    for caractere in listaExpressao:
        if parenteseFecha > parenteseAbre:
            validacao = False
            break
        if caractere == '(':
            parenteseAbre += 1
        elif caractere == ')':
            parenteseFecha += 1

if validacao:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
