# Ficha do Jogador

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)')


nome_jogador = str(input('Nome do Jogador: '))
gols_jogador = str(input('Gols do jogador: '))
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador.strip() == "":  #se for digitado apenas Enter
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)

