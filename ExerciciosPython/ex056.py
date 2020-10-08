somaidade = 0
idadeVelho = -1
mulheres20 = 0
for c in range(1, 5):
    print(f'\n===== {c}ª PESSOA =====')
    nome = str(input('Nome --> ')).strip()
    idade = int(input('Idade --> '))
    sexo = str(input('Sexo --> [M/F] ')).upper().strip()
    somaidade = somaidade + idade
    if (sexo == 'M') and (idade > idadeVelho):  # Verifica se a pessoa atual é do sexo masculino (M) e possui
        # a idade maior do que a mais velha atualmente
        nomeVelho = nome
        idadeVelho = idade
    if (sexo == 'F') and (idade < 20):  # Verifica se a pessoa atual é do sexo feminino (F) e possui idade menor
        # do que 20
        mulheres20 = mulheres20 + 1
print(f'MÉDIA DE IDADE --> {somaidade / 4:.2f}')
if idadeVelho > -1:  # Verifica se foi digitado alguma pessoa do sexo masculino
    print(f'IDADE DO HOMEM MAIS VELHO --> {idadeVelho} \nNOME DO HOMEM MAIS VELHO --> {nomeVelho} ')
print(f'TOTAL DE MULHERES COM MENOS DE 20 ANOS --> {mulheres20}')
