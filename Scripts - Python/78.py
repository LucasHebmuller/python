maior = menor = pos =  0
lista= []
for c in range(1,6):
    n= int(input('Digite um numero para a posicao {}: '.format(pos+1)))
    lista.append(n)
    if c==1:
        maior = n
        menor = n
    if n>maior:
        maior = n
    if n<menor:
        menor = n
    pos+= 1
print('='*20)
print(f'Voce digitou os valores {lista}')
print('O maior valor digitado foi o {} nas posicoes '.format(maior), end='')
for i, v in enumerate(lista):
    if v==maior:
        print(i+1,'')
print('O menor valor digitado foi o {} nas posicoes '.format(menor), end='')
for i, v in enumerate(lista):
    if v==menor:
        print(i+1,'')


