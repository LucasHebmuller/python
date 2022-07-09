def wikipedia(r):
    help(r)

resp = ''
while True:
    resp = str(input('Funcao ou Biblioteca > '))
    if resp.strip().lower() == 'fim':
        break
    else:
        wikipedia(resp)
    


