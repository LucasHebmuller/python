def maior(*num):
    print('-'*30)
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end= ' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print('Foram passados {} valores ao todo'.format(cont))
    print('O maior desses valores é o {}'.format(maior))
    print('-'*30)
    print()


maior(6,7,4,2,1,6)
maior(1,2,3)
maior()
maior(0)
        


    


