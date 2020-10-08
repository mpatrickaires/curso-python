a1 = int(input('Primeiro termo da P.A --> '))
r = int(input('Razão da P.A --> '))
for n in range(0, 10):
    print(a1, end=' -> ')
    a1 = a1 + r
print('FIM DA P.A')