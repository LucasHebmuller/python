galera=[]
dados=[]
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'Nn':
        break
print('='*20)
print(f'Ao todo, voce cadastrou {len(galera)} pessoas')
print('O maior peso foi de {}kg. Peso de '.format(maior), end='')
for c in galera:
    if c[1] == maior:
        print(f'{c[0]}', end=' ')
print()
print('O menor peso foi de {}kg. Peso de '.format(menor), end='')
for c in galera:
    if c[1] == menor:
        print(f'{c[0]}', end=' ')


