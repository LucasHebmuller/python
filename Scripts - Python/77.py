print('Vogais')
frase= ('Curso', 'em', 'Video')
for c in frase:
    print(f'\nNa palavra {c} temos ',end= ' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
