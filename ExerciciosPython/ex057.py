sexo = str(input('Qual é o seu sexo [M/F]? ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    print(f'\033[1;31m"{sexo}" NÃO É UM SEXO VÁLIDO! TENTE NOVAMENTE COM "M" OU "F"!\033[m')
    sexo = str(input('Qual é o seu sexo [M/F]? ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso!')
