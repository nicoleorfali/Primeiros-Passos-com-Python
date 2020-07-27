# Matrizes 3 x 3

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = soma3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o componente [{l}][{c}]: '))
print('-='*30)
for l in range(0,3):
    soma3 += matriz[l][2]
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print('-='*30)

#Valores pares
print(f'A soma dos valores pares da matriz é {soma}')

#Soma dos valores da terceira coluna
print(f'A soma dos elementos da terceira coluna é {soma3}')

#Maior valor da segunda linha
print(f'O maior elemento da segunda linha é {max(matriz[1])}')
