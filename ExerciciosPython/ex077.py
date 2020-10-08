palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for posicao in palavras:
    print(f'\nNa palavra {posicao.upper()} temos ', end='')

    for letra in posicao:  # Anda por todas as letras da palavra atribuida em 'posicao'
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
