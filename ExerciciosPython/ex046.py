from time import sleep  # Importa o sleep da biblioteca
print('CONTAGEM REGRESSIVA!')
for c in range(10, -1, -1):  # Faz o laço de repetição repetir de 10 até 0
    # Utiliza-se -1 como fim pois o laço de repetição FOR não considera o último número
    print(c)
    sleep(1)  # Faz o programa esperar 1 segundo
print('🎆 BUM 🎆')  # Print executável assim que o laço de repetição terminar
