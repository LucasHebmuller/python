matriz = [ [0,0,0] , [0,0,0] , [0,0,0] ]
for linha in range (0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input('Digite um valor para {},{}: '.format([linha],[coluna])))
print('='*32)
for linha in range (0,3):
    for coluna in range(0,3):
        print('{:^5}'.format(matriz[linha][coluna]),end='')
    print()


