import xixtema
from time import sleep

while True:
    resp = xixtema.menu(['Ver lista de pessoas','Cadastrar nova pessoa','Sair'])
    if resp == 1:
        xixtema.titulo('Opcão 1')
    elif resp == 2:
        xixtema.titulo('Opcão 2')
    elif resp == 3:
        xixtema.titulo('Saindo do sitema...')
        break
    else:
        print('Erro! Digite uma opção válida')
    sleep(2)


   
