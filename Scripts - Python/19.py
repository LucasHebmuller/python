import random
x1= input('Digite o nome da primera pessoa ')
x2= input('Digite o nome da segunda pessoa ')
x3= input('Digite o nome da terceira pessoa ')
x4=input('Digite o nome da quarta pessoa ')
lista= [x1,x2,x3,x4]
e= random.choice(lista)
print('A pessoa escolhida foi {} '.format(e))
