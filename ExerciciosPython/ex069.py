mais_de_18 = homem_cadastrado = mulheres_menos_de_20 = 0

while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)

    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()

    if idade >= 18:
        mais_de_18 += 1

    if sexo == 'M':
        homem_cadastrado += 1

    if idade < 20 and sexo == 'F':
        mulheres_menos_de_20 += 1

    print('-' * 30)

    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()

    if opcao == 'N':
        break

print(f'{" FIM DO PROGRAMA ":=^45}')
print(f'''TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {mais_de_18}
TOTAL DE HOMENS CADASTRADOS: {homem_cadastrado}
TOTAL DE MULHERES COM MENOS DE 20 ANOS: {mulheres_menos_de_20}''')
print('=' * 45)
