palavra = str(input('Digite uma palavra --> ')).strip().upper()
palavraSemEspaco = palavra.replace(' ', '')
inverso = ''
for c in range(len(palavraSemEspaco) - 1, - 1, - 1):
    inverso = inverso + palavraSemEspaco[c]
print(f'A palavra {palavraSemEspaco} invertida é {inverso}, ', end='')
if palavraSemEspaco == inverso:
    print('\nlogo \033[32mÉ UM PALÍNDROMO\033[m!')
else:
    print('\nlogo \033[31mNÃO É UM PALÍNDROMO\033[m!')
