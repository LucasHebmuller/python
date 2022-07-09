def linha():
    print('-'*30)


from time import sleep
galera = []
dados = []
maior = menor = cont = 0


linha()
print('{:^30}'.format('CADASTRO DE PESSOAS'))
linha()
while True:
    sleep(1)
    dados.append(str(input('Nome: ')).strip())
    dados.append(int(input('Peso: Kg ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados [1]
        if dados[1] < menor:
            menor = dados [1]
    galera.append(dados[:])
    dados.clear()
    cont += 1
    while True:
        resp = str(input('Voce quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        else:
            print('Digite uma resposta valida, por favor')
    linha()
    if resp == 'N':
        sleep(1)
        break
print(f'Ao todo, {cont} pessoas foram cadastradas.')
print(f'O maior peso registrado foi o de {maior}Kg, peso de',end=' ')
for c in galera:
    if c[1] == maior:
        print(f'{c[0]}.')
print(f'O menor peso registrado foi de {menor}Kg, peso de', end=' ')
for c in galera:
    if c[1] == menor:
        print(f'{c[0]}.')
sleep(2)
linha()
while True:
    question = str(input('Voce quer ver o cadastro completo? [S/N] ')).strip().upper()
    if question in 'SN':
        break
    else:
        print('Erro! Por favor, digite uma resposta valida')
linha()
if question == 'S':
    for pessoa, peso in galera:
        print(f'{pessoa} pesa {peso}Kg')
linha()
sleep(1)
print('Finalizando o programa',end=' ')
for c in range(1,4):
    print('.',end=' ')
    sleep(1)



