nome = str(input('Digite o seu nome --> ')).strip()
dividido = nome.split()
#Utilizando ~''.join()~:
SemEspaco = ''.join(dividido)
#Utilizando ~.replace()~:
#SemEspaco = nome.replace(' ', '')
print(f'----- {nome} ----- ')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')
print(f'Seu primeiro nome tem ao todo {nome.find(" ")} letras')
