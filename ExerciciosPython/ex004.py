print('===== DESAFIO 004 =====')

a = input('Digite algo: ')
print(f'----- INFORMAÇÕES SOBRE ~{a}~ -----')
# True = Verdadeiro/Sim
# False = Falso/Não
print(f'\033[30mTipo primitivo:\033[m {type(a)}')
print(f'\033[31mÉ alfabético?\033[m {a.isalpha()}')
print(f'\033[32mÉ alfanúmerico?\033[m {a.isalnum()}')
print(f'\033[33mÉ decimal?\033[m {a.isdecimal()}')
print(f'\033[34mÉ um dígito?\033[m {a.isdigit()}')
print(f'\033[35mÉ uma letra/palavra minúscula?\033[m {a.islower()}')
print(f'\033[36mÉ uma letra/palavra maiúscula?\033[m {a.isupper()}')
print(f'\033[37mÉ númerico?\033[m {a.isnumeric()}')
print(f'\033[1mÉ um espaço em branco?\033[m {a.isspace()}')
print(f'\033[4mEstá no formato "title()"?\033[m {a.istitle()}')
