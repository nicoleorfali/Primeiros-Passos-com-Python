# Jogo de Adivinhação Melhorado

from random import randint
from time import sleep #função que faz o computador esperar o argumento em segundos
print('Vamos brincar de adivinhação??? \nVou pensar um número inteiro entre 0 e 10...')
tentativa = 1
numero = randint(0,10)  # gera um inteiro entre 0 e 10
palpite = int(input('Que número eu pensei? '))
while palpite < 0 or palpite > 10:
    palpite = int(input('Você escolheu um número fora da faixa 0 e 10. \nTente novamente:  '))
print('Será que você acertou??? \nSERÁ???\n')
sleep(2) #faz esperar 3 segundos
while palpite != numero:
    tentativa += 1
    print(f'\nQue pena, você não acertou!')
    if palpite < numero:
        print('Mais...', end='')
        palpite = int(input('Tente novamente: '))
    else:
        print('Menos...', end='')
        palpite = int(input('Tente novamente: '))
print((f'\nParabéns, você acertou! Eu realmente pensei em {palpite}. \nVocê fez {tentativa} tentativas.')) 
  