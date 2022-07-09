def dobro(n):
    return n*2


def metade(n):
    return n/2


def aumentar(n,taxa):
    x = n + (n*taxa/100)
    return x


def diminuir(n,taxa):
    x = n - (n*taxa/100)
    return x


def resumo(n,a=0,d=0):
    print('-'*30)
    print('{:^30}'.format('Resumo do valor'))
    print('-'*30)
    print('Preco analisado: ',end='')
    print('{:>10.2f}'.format(n))
    print('Dobro do preco: ',end='')
    print('{:>11.2f}'.format(dobro(n)))
    print('Metade do preco: ',end='')
    print('{:>10.2f}'.format(metade(n)))
    print(a,'% do aumento: ',end='')
    print('{:>10.2f}'.format(aumentar(n,a)))
    print(d,'% de desconto: ',end='')
    print('{:>9.2f}'.format(diminuir(n,d)))
