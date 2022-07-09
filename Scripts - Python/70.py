print('#'*30)
print('{:^30}'.format('Loja da boa'))
print('#'*30)
ptot = pmil = menor = cont = 0
barato = ''
while True:
    p= int(input('Qual o preco do produto? '))
    n= str(input('Qual o nome do produto? ')).strip().lower()
    r= str(input('Voce quer continuar? [S/N] ')).strip().upper()
    ptot+= p
    cont+= 1
    if cont==1:
        menor = p
        barato = n
    else:
        if p<menor:
            menor = p
            barato = n
    if p>1000:
        pmil+= 1
    if r=='N':
        break
    print('#'*30)
print('#'*30)
print('Ao todo a compra sai por R${} '.format(ptot))
print(f'{pmil} produtos saem por mais de R$1000')
print('O produto mais barato é {}, por R${}'.format(barato,menor))
    
    
    
