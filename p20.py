# Análise de strings
nome_completo = str(input('Digite o seu nome: ')).strip() #strip tirando espaços indesejáveis
nc = nome_completo.lower().split()
if 'silva' in nc:
    print('Você tem Silva no nome')
else:
    print('Você não tem Silva no nome')
