# Manipulação de números
numero = int(input('Digite um número entre 0 e 9999: ')) 
u = numero // 1 % 10 #divisão inteira e módulo (resto de divisão)
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
