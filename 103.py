def ficha(nome = '<desconhecido>' , gols = 0):
    print('O jogador {} fez {} gol(s no campeonato'.format(nome,gols))

    
n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
