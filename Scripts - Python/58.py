t= 0
from random import choice
opcoes= [1,2,3,4,5,6,7,8,9,10]
print('='*55)
print('{:^55}'.format('Jogo da adivinhacao'))
print('='*55)
print('Pensei em um numero entre 1 e 10... tente adivinhar!')
chute= int(input('Tente adivinhar o numero que o computador escolheu: '))
print('='*55)
r= choice(opcoes)
while chute != r:
    t+= 1
    print('Errrrooooooouu')
    if chute>r:
        print('Menos...')
    else:
        print('Mais...')
    print('='*55)
    chute= int(input('Tente adivinhar o numero que o computador escolheu: '))
print('Parabens, voce acertou! Voce precisou de {} tentativas'.format(t))
    
