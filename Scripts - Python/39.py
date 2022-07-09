nasc= int(input('Em que ano voce nasceu? '))
idade= 2022-nasc
print('Quem nasceu em {} faz {} anos em 2022'.format(nasc,idade))
if idade>18:
    print('Voce ja deveria ter se alistado ha {} ano(s)'.format(idade-18))
    print('Seu alistamento foi em {}'.format(nasc+18))
elif idade<18:
    print('Voce deve se alistar em {} ano(s)'.format(18-idade))
    print('Sei alistamento sera em {}'.format(nasc+18))
else:
    print('Voce deve se alistar nesse ano, 2022')

