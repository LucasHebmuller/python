def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Erro! Digite um numero inteiro valido, por favor. ')
            continue
        else:
            return n
   

def LeiaReal(txt):
    while True:
        try:
            n = float(input(txt))
        except:
            print('Erro! Digite um numero real valido, por favor. ')
            continue
        else:
            return n
  

i = LeiaInt('Digite um numero Inteiro: ')
r = LeiaReal('Digite um numero Real: ')
print(f'Voce digitou o numero Inteiro {i} e o numero Real {r}')
