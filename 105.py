def notas(*n , sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 8:
            r['Situation'] = 'BOA'
        elif r['Media'] >= 6:
            r['Situation'] = 'RAZOAVEL'
        else:
            r['Situation'] = 'RUIM'
    return r


resp = notas(7,8,9.2,sit=True)
print(resp)
