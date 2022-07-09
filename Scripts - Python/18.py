import math
a= float(input('Digite um angulo '))
s= math.sin(math.radians(a))
c= math.cos(math.radians(a))
t= math.tan(math.radians(a))
print('Em relacao ao angulo {}, seu seno vale {:.2f}, seu cosseno vale {:.2f} e sua tangente vale{:.2f}'.format(a,s,c,t))
