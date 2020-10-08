a1 = float(input('1º Termo da P.A. --> '))
r = float(input('Razão da P.A. --> '))
print(f'{" 10 PRIMEIROS TERMOS DA P.A. ":=^55} \n[', end='')
cont = 1
while cont <= 10:
    if cont != 10:
        print(a1, end='; ')
        a1 = a1 + r
        cont = cont + 1
    else:
        print(a1, end=']')
        cont = cont + 1
