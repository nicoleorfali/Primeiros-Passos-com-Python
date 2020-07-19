# Mais de manipulação de strings
nome_completo = str(input('Digite o seu nome: ')).strip() #strip tirando espaços indesejáveis
nc = nome_completo.split()
print(f'Nome:  {nc[0].capitalize()}')
print(f'Sobrenome: {nc[-1].capitalize()}')
