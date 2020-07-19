# Jogo da Adivinhação 
from random import randint
from time import sleep #função que faz o computador esperar o argumento em segundos

print('Vamos brincar de adivinhação??? \nVou pensar um número inteiro entre 0 e 5...')
numero = randint(0,5)
palpite = int(input('Que número eu pensei? '))
while palpite < 0 or palpite > 5:
  palpite = int(input('Você escolheu um número fora da faixa 0 e 5 \nTente novamente:  '))
print('Será que você acertou??? \nSERÁ???\n\n')
sleep(2) #faz esperar 3 segundos
if palpite == numero:
  print((f'Parabéns, você acertou!\nEu realmente pensei em {palpite}')) 
else:
  print(f'Que pena, você não acertou!\nEu pensei em {numero}')
