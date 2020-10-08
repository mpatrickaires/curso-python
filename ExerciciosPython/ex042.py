print('\033[34m=-=' * 15)
print('\033[35mA N A L I S A D O R  D E  T R I Â N G U L O')
print('\033[34m=-=' * 15)
l1 = float(input('\033[mComprimento da 1ª reta --> '))
l2 = float(input('Comprimento da 2ª reta --> '))
l3 = float(input('Comprimento da 3ª reta --> '))
if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2): # Verificar se o tamanho das retas permitem formar um triângulo.
    if (l1 == l2) and (l1 == l3): # Verificar se todos os lados são iguais.
        print('Essas retas \033[32mPODEM\033[m formar um \033[33mTRIÂNGULO EQUILÁTERO\033[m!')
    elif (l1 == l2) or (l2 == l3) or (l1 == l3): # Verificar se só possui dois lados iguais.
        print('Essas retas \033[32mPODEM\033[m formar um \033[34mTRIÂNGULO ISÓSCELES\033[m!')
    else: # Se as duas condições acima não acontecerem, logo todos os lados são diferentes.
        print('Essas retas \033[32mPODEM\033[m formar um \033[35mTRIÂNGULO ESCALENO\033[m!')
else: # Os tamanhos das retas não permitem formar um triângulo.
    print('Essas retas \033[31mNÃO PODEM\033[m formar um TRIÂNGULO!')