distancia = float(input('Digite a distância da viagem em Km --> '))
if distancia <= 200:
    valor = distancia * 0.50
    print('===== GRANTURISMO VIAGENS =====')
    print(f'----- DISTÂNCIA -----> {distancia}Km')
    print(f'-----   VALOR   -----> R${valor:.2f}')
    print('=' * 31)
else:
    valor = distancia * 0.45
    print(f'===== GRANTURISMO VIAGENS =====')
    print(f'----- DISTÂNCIA -----> {distancia}Km')
    print(f'-----   VALOR   -----> R${valor:.2f}')
    print('=' * 31)
