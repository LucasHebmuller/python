lista=[]
pares=[]
impares=[]
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n%2!=0:
        impares.append(n)
    else:
        pares.append(n)
    r = str(input('Voce quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('-'*20)
print(f'A lista completa e {lista}')
print(f'Os pares dessa lista sao {pares}')
print(f'Os impares dessa lista sao {impares}')
