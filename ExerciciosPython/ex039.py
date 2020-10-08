from datetime import date
from playsound import playsound
anonasc = int(input('Digite o seu ano de nascimento --> '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade < 18: # Verifica se o usuário é menor de 18 anos
    if 18 - idade == 1:
        print(f'\033[30mAinda falta 1 ano para você se alistar, fique tranquilo enquanto pode!')
    else:
        print(f'\033[30mAinda faltam {18 - idade} anos para você se alistar, fique tranquilo enquanto pode!')
        print(f'Seu alistamento será em {anoatual + (18 - idade)}.')
elif idade == 18: # Verifica se o usuário tem exatamente 18 anos
    print(f'\033[36mJá tá na hora de se alistar rapaz, vai logo pro quartel capinar mato!')
elif idade > 18: # Verifica se o usuário tem mais de 18 anos. Pode ser substituido por else
    if abs(18 - idade) == 1:
        print(f'\033[31mJá passou 1 ano do seu prazo para se alistar.')
    else:
        print(f'\033[31mJá passaram {idade - 18} anos do seu prazo para se alistar.')
    print(f'Você tinha que ter se alistando em {anoatual - (idade - 18)}')
    print(f'Corre que o camburão vai ir te buscar!')
    #playsound('ex039.mp3') # Aqui é para tocar uma sirene de polícia
