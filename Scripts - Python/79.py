lista= []
while True:
    n= int(input('Digite um valor: '))
    if n in lista:
        print('Valor repetido, erro na hora de adicionar a lista')
    else:
        print('Valor adicionado com sucesso')
        lista.append(n)
    r= str(input('Voce quer continuar? [S/N] ')).upper().strip()
    if r=='N':
        break
lista.sort()
print(f'Voce digitou os valores {lista}')
