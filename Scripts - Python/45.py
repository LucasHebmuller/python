from random import choice
print('='*30)
print('{:^30}'.format('Pedra Papel Tesoura'))
print('='*30)
opcao= int(input('''Escolha uma das opcoes abaixo para jogar contra o computador:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Sua jogada: '''))
a= 'Pedra'
b= 'Papel'
c= 'Tesoura'
jogadas=[a,b,c]
pc= choice(jogadas)

print('='*30)

print('O computador escolheu {}'.format(pc))
if opcao==1:
    print('O jogador escolheu Pedra')
elif opcao==2:
    print('O jogador escolheu Papel')
else:
    print('O jogador escolheu Tesoura')
    
print('='*30)

if opcao==1:
    if pc==a:
        print('Empate')
    elif pc==b:
        print('O computador venceu')
    else:
        print('O jogador venceu')
elif opcao==2:
    if pc==a:
        print('O jogador venceu')
    elif pc==b:
        print('Empate')
    else:
        print('O computador venceu')
else:
    if pc==a:
        print('O computador venceu')
    elif pc==b:
        print('O jogador venceu')
    else:
        print('Empate')



