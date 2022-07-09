def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        return 'Com {} anos, o voto é obrigatório'.format(idade)
    elif idade >= 16:
        return 'Com {} anos, o voto é facultativo'.format(idade)
    else:
        return 'Com {} anos, nao se pode votar'.format(idade)


nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))

