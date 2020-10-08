peso = float(input('Peso (kg)  --> '))
altura = float(input('Altura (m) --> '))
imc = peso / pow(altura, 2) # pow() é a função para elevar um número ao quadrado --> pow(número, expoente)
print(f'IMC: {imc:.1f}')
if peso < 0 or altura < 0: # Verifica se a pessoa digitou valores inválidos (peso e/ou altura negativos)
    print('\033[31mERRO: VALORES INVÁLIDOS \nO PESO E/OU ALTURA NÃO PODEM SER MENORES DO QUE 0')
# imc = peso / (altura * altura) OU peso / (altura ** 2) --> outra possibilidade de cálculo
elif imc < 18.5: # Verifica se o IMC da pessoa está abaixo de 18.5
    print(f'Você está \033[31mABAIXO DO PESO\033[m!')
elif imc < 25: # Verifica se o IMC da pessoa está entre 18.5 e 24.9
    print(f'Você está com o \033[36mPESO IDEAL\033[m!')
elif imc < 30: # Verifica se o IMC da pessoa está entre 25 e 29.9
    print(f'Você está com \033[32mSOBREPESO\033[m!')
elif imc < 40: # Verifica se o IMC da pessoa está entre 30 e 39.9
    print(f'Você está com \033[33mOBESIDADE\033[m!')
else: # Bloco executável caso o IMC da pessoa esteja igual ou acima de 40
    print(f'Você está com \033[31mOBESIDADE MÓRBIDA\033[m!')
