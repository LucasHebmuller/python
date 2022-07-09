matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = coluna3 = linha2 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if matriz[linha][coluna]%2==0:
            pares += matriz[linha][coluna]
        if coluna == 2:
            coluna3 += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                linha2 = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > linha2:
                    linha2 = matriz[linha][coluna]
print('='*20)
for linha in range (0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()
print('='*20)
print('A soma dos numeros pares foi: {}'.format(pares))
print('A soma dos valores da terceira coluna foi: {}'.format(coluna3))
print('O maior valor da segunda linha foi: {}'.format(linha2))
