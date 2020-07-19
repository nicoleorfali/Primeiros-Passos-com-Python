# Soma dos números digitados pelo usuário

soma = 0
for i in range(6):
    n1 = int(input('Digite um número: '))
    if (n1 % 2) == 0:
        soma += n1
print(f'A soma dos números pares digitados foi: {soma}')
