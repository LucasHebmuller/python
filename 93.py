dados = {}
lista = []
tot = 0
dados['Nome'] = str(input('Nome do jogador: '))
dados['Partidas'] = int(input('Quantas partidas {} jogou? '.format(dados['Nome'])))
for c in range(1,dados['Partidas']+1):
    x = int(input(f'    Quantos gols na partida {c}? '))
    lista.append(x)
    tot += x
dados['Gols'] = lista
dados['Total'] = tot
print('='*30)
print(dados)
print('='*30)
for k,v in dados.items():
    print(f'{k} tem valor {v}')
print('='*30)
print('O jogador {} jogou {} partidas'.format(dados['Nome'],dados['Partidas']))
for c in range(0,dados['Partidas']):
    print(f'    Na partida {c+1} fez {lista[c]}')
    
