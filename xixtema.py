def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('Erro! Digite uma opção válida')
            continue
        except(KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = LeiaInt('Sua opção: ')
    return opc

