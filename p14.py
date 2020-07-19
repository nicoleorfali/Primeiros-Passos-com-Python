# Parte inteira de um número
from math import ceil, floor, trunc #dá para chamar apenas as funções que vamos usar

n = float(input('Digite um valor: '))
print(f'A parte inteira de {n} é {trunc(n)}')
# ou dá para fazer com a função builtin int()
print(f'A parte inteira de {n} é {int(n)}')
