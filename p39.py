# Pedra, papel ou tesoura

from random import choice, shuffle, randint
from time import sleep

print('{:=^60}'.format(' PEDRA, PAPEL OU TESOURA ')) #para centralizar a string
opcao = str(input('\nQual sua escolha: PEDRA, PAPEL ou TESOURA? ' )).lower()
jogo = ['pedra', 'papel', 'tesoura']
escolha_computador = choice(jogo)
print('Será que você ganhou??? \nSERÁ???\n\n')
sleep(1) #faz esperar 1 segundos
if opcao == escolha_computador:
    print(f'Empate! Ambos escolhemos {opcao.upper()}!')
elif opcao == 'papel' and escolha_computador == 'tesoura':
    print(f'Você perdeu! Eu escolhi {escolha_computador.upper()} e você escolheu {opcao.upper()}!!!')
elif opcao == 'papel' and escolha_computador == 'pedra':
    print(f'Você ganhou! Eu escolhi {escolha_computador.upper()} e você escolheu {opcao.upper()}!!!')
elif opcao == 'pedra' and escolha_computador == 'papel':
    print(f'Você perdeu! Eu escolhi {escolha_computador.upper()} e você escolheu {opcao.upper()}!!!')
elif opcao == 'pedra' and escolha_computador == 'tesoura':
    print(f'Você ganhou! Eu escolhi {escolha_computador.upper()} e você escolheu {opcao.upper()}!!!')
elif opcao == 'tesoura' and escolha_computador == 'pedra':
    print(f'Você perdeu! Eu escolhi {escolha_computador.upper()} e você escolheu {opcao.upper()}!!!')
elif opcao == 'tesoura' and escolha_computador == 'papel':
    print(f'Você ganhou! Eu escolhi {escolha_computador.upper()} e você escolheu {opcao.upper()}!!!')
else:
    print(f'Você digitou uma palavra inválida. Tente novamente!')
