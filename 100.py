from random import randint
from time import sleep
numeros = []
def sorteia():
    print('Sorteando 5 valores para a lista... ',end='')
    for c in range (1,6):
        numeros.append(randint(1,10))
    for i,v in enumerate(numeros):
        print(f'{v} ', end='')
        sleep(0.4)
    print('Pronto!')
def somaPar():
    pares = 0
    for i,v in enumerate(numeros):
        if v%2 == 0:
            pares += v
    print(f'Somando os valores pares de {numeros}, temos {pares}.')

sorteia()
somaPar()
        





