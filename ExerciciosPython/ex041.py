from datetime import date
anonasc = int(input('Digite seu ano de nascimento --> '))
anoatual = date.today().year
idade = anoatual - anonasc
if anonasc > anoatual:
    print('\033[31mO ANO DE NASCIMENTO NÃO PODE SER MAIOR QUE O ANO ATUAL. \nTENTE NOVAMENTE!')
elif idade <= 9:
    print(f'\033[30mIDADE: {idade} ANOS \nCATEGORIA: MIRIM')
elif idade <= 14:
    print(f'\033[32mIDADE: {idade} ANOS \nCATEGORIA: INFANTIL')
elif idade <= 19:
    print(f'\033[33mIDADE: {idade} ANOS \nCATEGORIA: JUNIOR')
elif idade <= 25:
    print(f'\033[34mIDADE: {idade} ANOS \nCATEGORIA: SÊNIOR')
else:
    print(f'\033[35mIDADE: {idade} ANOS \nCATEGORIA: MASTER')
