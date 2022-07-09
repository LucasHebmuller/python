def contador(i,f,p):
    """
    i = inicio da contagem
    f = fim da contagem
    p = passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')


contador(1,10,1)
help(contador)
