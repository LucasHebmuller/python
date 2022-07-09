import moeda
def LeiaDinheiro(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'Erro! {entrada} é um valor inválido.')
        else:
            ok = True
            return float(entrada)


p = LeiaDinheiro('Digite um preco: ')
moeda.resumo(p)
