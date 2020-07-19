# Cálculo de fatorial

print('{:=^40}'.format(' CÁLCULO DE FATORIAL COM WHILE')) #para centralizar a string
n1 = int(input('Informe o número: '))
i = n1
f = n1
while i - 1 > 0:
  f *= (i-1)
  i -= 1
print(f'O fatorial de {n1} é {f}\n')

print('{:=^40}'.format(' CÁLCULO DE FATORIAL COM FOR')) #para centralizar a string

f = n1
for i in range(n1 -1, 1, -1):
  f *= (i)
print(f'O fatorial de {n1} é {f}')
