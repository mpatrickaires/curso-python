listaAlunos = list()

while True:
    aluno = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    listaAlunos.append([aluno, [nota1, nota2], media])

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break

print('-=' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for numero, aluno in enumerate(listaAlunos):
    print(f'{numero:<4}{aluno[0]:<10}{aluno[2]:>6.1f}')


while True:
    print('-' * 25)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    while opcao < 0 or opcao > len(listaAlunos) - 1:
        opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print(f'Notas de {listaAlunos[opcao][0]} são {listaAlunos[opcao][1]}')

print('FINALIZANDO... \n<<< VOLTE SEMPRE >>>')
