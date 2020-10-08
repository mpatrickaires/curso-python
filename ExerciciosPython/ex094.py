galera = list()
pessoa = dict()
somaIdade = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()

    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('ERRO! Por favor, digite apenas M ou F. \nSexo: [M/F] ')).strip().upper()

    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']

    galera.append(pessoa.copy())  # Insere uma cópia do dicionário atual na lista 'galera'

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('ERRO! Responda apenas S ou N. \nQuer continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break

print('-=' * 30)
print(f'A) O grupo tem {len(galera)} pessoas.')

mediaIdade = somaIdade / len(galera)
print(f'B) A média de idade é de {mediaIdade:5.2f} anos.')

print('C) As mulheres cadastradas foram ', end='')
for individuo in galera:  # Anda por todos os dicionários 'pessoa' na lista 'galera'
    if individuo['sexo'] == 'F':
        print(individuo['nome'], end=' ')

print('\nD) Lista de pessoas que estão acima da média: \n')
for individuo in galera:  # Anda por todos os dicionários 'pessoa' na lista 'galera'
    # Confere se a idade no dicionário atual é maior que a média
    if individuo['idade'] >= mediaIdade:
        # Anda por todas as chaves e seus respectivos valores no dicionário atual:
        for key, value in individuo.items():  
            print(f'  => {key} = {value}; ', end='')
        print()

print('<< ENCERRADO >>')
