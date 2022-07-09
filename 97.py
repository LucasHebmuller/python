def mensagem(txt):
    tam = len(txt)+4
    print('='*tam)
    print(f'  {txt}')
    print('='*tam)


x = str(input('Digite uma mensagem: '))
mensagem(x)
    
