def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1

    
valores = [5,6,4,2,1]
dobra(valores)
print(valores)
