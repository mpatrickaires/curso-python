peso = float(input('Peso da 1ª pessoa (kg) --> '))
maior = peso
menor = peso
# É preciso atribuir valor à variável MENOR antes de entrar no laço de repetição, pois não se sabe quais vão ser
# os valores inseridos, impossibilitando de dar qualquer valor aleatório para o menor peso
for c in range(2, 6):
    peso = float(input(f'Peso da {c}ª pessoa (kg) --> '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'MAIOR PESO --> {maior} kg \nMENOR PESO --> {menor} kg')

'''OUTRA FORMA POSSÍVEL DE FAZER O ALGORITMO:
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa (kg) --> '))
    if c == 1:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'MAIOR PESO --> {maior} kg \nMENOR PESO --> {menor} kg')'''