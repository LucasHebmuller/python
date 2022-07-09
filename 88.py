from random import randint
cont = 0
print('='*20)
print('{:^20}'.format('MEGA SENA'))
print('='*20)
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-----Sorteando os Jogos-----')
for c in range(1,jogos+1):
    sorteio = []
    while True:
        n = randint(1,60)
        if n not in sorteio:
            sorteio.append(n)
            cont += 1
        if cont >= 6:
            break
    print(f'Jogo {c}: ',sorteio)
    sorteio.clear()
    cont = 0
print('-----Boa Sorte-----')

