aluno = {}
aluno['Nome'] = str(input('Nome: ')).title().strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado(a)'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'

print('-=' * 30)
for chave, valor in aluno.items():
    print(f'  - {chave} é igual a {valor}')
