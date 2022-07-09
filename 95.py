dados = {}
lista = []
gol = []
tot = 0
while True:
    dados.clear()
    tot = 0
    gol = []
    dados['Nome'] = str(input('Nome do jogador: '))
    dados['Partidas'] = int(input('Quantas partidas {} jogou? '.format(dados['Nome'])))
    for c in range(1,dados['Partidas']+1):
        x = int(input(f'    Quantos gols na partida {c}? '))
        gol.append(x)
        tot += x
    dados['Gols'] = gol
    dados['Total'] = tot
    lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp == 'N':
        break
    print('-'*60)
print('='*60)
print('Cod' , end=' ')
for c in dados.keys():
    print(f'{c:<12}',end='')
print()
print('-'*60)
for k,v in enumerate(lista):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<12}',end='')
    print()
print('='*60)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(dados):
        print('ERRO! Nao ha jogador com esse codigo, tente novamente.')
    else:
        print(f'Sobre o {lista[busca]["Nome"]}')
        for i,g in enumerate(lista[busca]["Gols"]):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-'*60)
print('<<<ENCERRADO>>>')
            

    
        
