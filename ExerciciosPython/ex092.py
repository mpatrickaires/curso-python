from datetime import datetime
pessoa = {'Nome': str(input('Nome: ')).strip().title(),
          'Idade': datetime.today().year - int(input('Ano de Nascimento: ')),
          'CTPS': int(input('Carteira de Trabalho (0 se não tem): '))}

if pessoa['CTPS'] > 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (35 - (datetime.today().year - pessoa['Contratação']))

print('-=' * 20)
for key, value in pessoa.items():
    print(f'  - {key} tem o valor {value}')
