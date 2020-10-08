frase = str(input('Digite uma frase --> ')).upper().strip()
print(f'Total de letras "A" na frase  --> {frase.count("A")}')
print(f'Posição da primeira letra "A" --> {frase.find("A") + 1}')
print(f'Posição da última letra "A"   --> {frase.rfind("A") + 1}')
