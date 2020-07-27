# Cadastro do Jogador de Futebol

jogador = {}
gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {i+1}ª partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-'*35)
#Primeira solução
print(jogador)
print('=-'*35)

#Segunda solução
for i, j in jogador.items():
    print(f'O campo {i} tem valor {j}')
print('=-'*35)

#Terceira solução
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, j in enumerate(jogador['gols']):
    print(f'  => Na {i+1}ª partida ele fez {j} gols.')
print(f'Foi um total de {jogador["total"]} gols.')