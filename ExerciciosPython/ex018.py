from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'----- ÂNGULO DE {angulo}º -----')
print(f'Valor do seno     --> {seno:.2f}')
print(f'Valor do cosseno  --> {cosseno:.2f}')
print(f'Valor da tangente --> {tangente:.2f}')
