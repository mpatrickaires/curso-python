a1 = float(input('1º Termo da P.A. --> '))
r = float(input('Razão da P.A. --> '))
inicio = 10
termos = inicio
while inicio > 0:
    print(f'[{a1}] -> ', end='')
    a1 = a1 + r
    inicio = inicio - 1
    if inicio == 0:
        print('PAUSA')
        inicio = int(input('Digite mais quantos termos dessa P.A. você deseja ver --> '))
        termos = termos + inicio
print(f'\033[1;31mProgressão finalizada com {termos} termos mostrados!')
