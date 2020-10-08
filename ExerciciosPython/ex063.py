inicio = 1
a = 0
b = 1
c = a + b
fim = int(input('Digite quantos termos da sequência de Fibonacci você quer ver --> '))
while inicio <= fim:
    print(f'{a} -> ', end='')
    a = b
    b = c
    c = a + b
    inicio = inicio + 1
print('FIM')
