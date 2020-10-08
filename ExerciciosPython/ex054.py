from datetime import date
anoatual = date.today().year  # Atribuiu para a variável ANOATUAL o ano atual do sistema
# É preciso declarar as variáveis MAIOR e MENOR antes de entrar no laço de repetição:
maior = 0
menor = 0
for c in range(1, 8):  # Executa o laço de repetição de 1 até 7
    anonasc = int(input(f'Data de nascimento da {c}ª pessoa --> '))
    if anoatual - anonasc >= 21:  # Verifica se, com o ano atual da pessoa, ela já tem mais de 21 anos
        maior = maior + 1  # Adiciona mais 1 para a variável MAIOR caso a pessoa tenha mais de 21 anos
    else:  # Bloco executável se, com o ano atual da pessoa, ela tenha menos de 21 anos
        menor = menor + 1  # Adiciona mais 1 para a variável MENOR caso a pessoa tenha menos de 21 anos
if maior > 1:  # Verifica se mais de 1 pessoa atingiu a maioridade, ficando as palavras no plural
    print(f'{maior} pessoas já atingiram a maioridade.')
else:
    print(f'{maior} pessoa já atingiu a maioridade.')
if menor > 1:  # Mesmo conceito do IF MAIOR > 1
    print(f'{menor} pessoas ainda são de menor.')
else:
    print(f'{menor} pessoa ainda é de menor.')
