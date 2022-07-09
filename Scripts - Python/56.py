mediaidade=0
menosvinte=0
nomehomemmaisvelho= ''
idadehomemmaisvelho= 0
print('='*40)
print('{:^40}'.format('Analisador de pessoas'))
print('='*40)
for c in range(1,5):
    nome= str(input('Qual é o seu nome? ')).strip()
    idade= int(input('Qual é a sua idade? '))
    sexo= str(input('Você é do sexo masculino ou feminino? ')).strip().lower()
    print('='*40)
    mediaidade+= idade
    if sexo == ('feminino'):
        if idade < 20:
            menosvinte+= 1
    if sexo ==('masculino'):
        if idade>idadehomemmaisvelho:
            idadehomemmaisvelho=idade
            nomehomemmaisvelho=nome
mediaidade = mediaidade/4
print('A média de idade do grupo é:{:.1f}'.format(mediaidade))
print('Tem {} mulheres com menos de vinte anos no grupo'.format(menosvinte))
print('O homem mais velho do grupo se chama {}'.format(nomehomemmaisvelho))
