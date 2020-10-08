print('=-=' * 20)
print('A N A L I S A D O R  D E  T R I Â N G U L O')
print('=-=' * 20)
reta1 = float(input('Comprimento da 1ª reta --> '))
reta2 = float(input('Comprimento da 2ª reta --> '))
reta3 = float(input('Comprimento da 3ª reta --> '))
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Essas retas PODEM formar um TRIÂNGULO!')
else:
    print('Essas retas NÃO PODEM formar um TRIÂNGULO!')
