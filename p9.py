# Programa que calcula a tabuada
n = int(input('Digite um valor inteiro entre 1 e 9: '))
print('_' * 12) #faz os tracinhos 12 vezes
print(f'Tabuada de {n}')
print('-' * 12)
for i in range(10):
  i += 1
  print(f'{n:2} x {i:2} = {n*i:2}')
   