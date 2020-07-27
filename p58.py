# Função Notas
def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if r['média'] >= 7:
        r['situação'] = 'Aprovado'
    elif 5 <= r['média'] <7:
        r['situação'] = 'Em recuperação'
    else:
        r['situação'] = 'Reprovado'
    return r


#Programa Principal
resp = notas(5.5, 6, 9, 10)
print(resp)