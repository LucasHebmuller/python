lista=[]
cont= 0
while True:
    n= int(input('Digite um numero: '))
    lista.append(n)
    r= str(input('Voce quer continuar? [S/N] ')).strip().upper()
    cont+=1
    if r == 'N':
        break
lista.sort(reverse=True)
print('='*30)
print('A lista contem {} elementos'.format(cont))
print('Os valores em ordem decrescente sao {}'.format(lista))
if 5 in lista:
    print('O numero 5 foi encontrado na lista')
else:
    print('O numero 5 nao foi encontrado na lista')
    
