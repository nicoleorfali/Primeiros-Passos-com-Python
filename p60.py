# Jogo de Dados

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = {}
print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    #sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #retorna uma lista
print('='*30)
print(f'{"Ranking dos Jogadores":^30}')
print('='*30)
for i, j in enumerate(ranking):
    print(f'{i+1}° lugar: {j[0]} com {j[1]}')
