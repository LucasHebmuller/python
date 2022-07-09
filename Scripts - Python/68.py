from random import choice
opc = [0,1,2,3,4,5]
v = pc = j = s = 0
print('{:^35}'.format('Jogue par ou impar contra o computador ate perder'))
print('='*35)
while True:
    j= int(input('Escolha um numero para jogar: '))
    PI= str(input('Par ou impar? ')).lower().strip()
    pc= choice(opc)
    s = pc+j
    if s%2==0:
        print('Voce jogou {} e o computador jogou {}. A soma da {}, logo um numero par'.format(j,pc,s))
    else:
        print('Voce jogou {} e o computador jogou {}. A soma da {}, logo um numero impar'.format(j,pc,s))
    if PI=='par' and s%2==0:
        print('Voce ganhou')
        v+=1
    elif PI=='impar' and s%2!=0:
        print('Voce ganhou')
        v+=1
    elif PI=='par' and s%2!=0:
        print('Voce perdeu')
        break
    elif PI=='impar' and s%2==0:
        print('Voce perdeu')
        break
    print('='*35)
print('='*35)
print(f'Jogo finalizado, voce conseguiu {v} vitorias seguidas')
    
        
