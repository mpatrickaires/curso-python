print('=' * 35)
print(f'{"BANCO CEV":^35}')
print('=' * 35)

valor = int(input('Que valor você quer sacar? R$'))
while True:

    if valor // 50 > 0:
        print(f'Total de {valor // 50} cédula(s) de R$50.00')
        valor = valor % 50

    if valor // 20 > 0:
        print(f'Total de {valor // 20} cédula(s) de R$20.00')
        valor = valor % 20

    if valor // 10 > 0:
        print(f'Total de {valor // 10} cédula(s) de R$10.00')
        valor = valor % 10

    if valor // 1 > 0:
        print(f'Total de {valor // 1} cédula(s) de R$1.00')

    break

print('=' * 35)
print('Volte sempre ao banco CEV! Tenha um bom dia!')
