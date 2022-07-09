try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite mais um numero: '))
    r = a/b
except:
    print('Houve um problema na execucao do programa...')
else:
    print(f'O resultado da divisao de {a} por {b} é {r:.1f}')
finally:
    print('Programa finalizado')
