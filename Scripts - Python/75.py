n= (int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')))
print('O numero 9 apareceu {} vezes'.format(n.count(9)))
tres = n.count(3)
if tres > 0:
    print('O numero 3 apareceu na posicao {}'.format(n.index(3)+1))
else:
    print('O numero 3 nao apareceu ')
print('Os numeros pares que aparecem foram: ',end='')
for c in n:
    if c%2==0:
        print(c, end=' ')



                                                                                                                                                
