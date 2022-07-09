nasc= int(input('Em que ano o atleta nasceu? '))
idade= 2022-nasc
print('O atleta faz {} anos este ano.'.format(idade))
if idade<=9:
    print('O atleta esta na categoria mirim')
elif idade<=14:
    print('O atleta esta na categoria infantil')
elif idade<=19:
    print('O atleta esta na categoria junior')
elif idade<=25:
    print('O atleta esta na categoria senior')
else:
    print('O atleta esta na categoria master')
