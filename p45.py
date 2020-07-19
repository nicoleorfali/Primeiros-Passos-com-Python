# Números primos

soma = 0
num = int(input('Digite um número: '))
for i in range(1, num):
    if num % i == 0:
        soma += 1 
if soma > 1:
    print(f'{num} não é primo')
else:
    print(f'{num} é primo')
