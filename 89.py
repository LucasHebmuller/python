lista = []
while True:
    dados = []
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Nota 1: ')))
    dados.append(int(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    r = str(input('Voce quer continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
print('='*30)
print('No. Nome        Media')
print('---------------------')
for c in range(0,len(lista)):
    print('{}{:^5}{:>15}'.format((c),(lista[c][0]),((lista[c][1]+lista[0][2])/2)))
print('---------------------')
while True:
    n = int(input('Voce quer ver as notas de qual aluno? (999 para) '))
    if n == 999:
        print('---------------------')
        break
    else:
        print(lista[n][1],end='   ')
        print(lista[n][2])
    print('---------------------')
print('Programa finalizado')
    
