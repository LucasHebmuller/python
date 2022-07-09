frase= str(input('Digite uma frase ')).upper().strip()
print('A letra A aparece {} vezes na frase. '.format(frase.count('A')))
print('A primeira posicao em que A aparece na frase e: {}' .format(frase.find('A')+1))
print('A primeira ultima em que A aparece na frase e: {}' .format(frase.rfind('A')+1))
