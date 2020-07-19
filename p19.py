# Análise de strings
cidade = str(input('Digite o nome da cidade em que você nasceu: ')).strip() #strip elimina espaços indesejáveis
c = cidade.lower()
if 'santo' in c.split()[0]:
    print('A cidade que você nasceu começa com Santo')
else:
    print('A cidade que você nasceu não começa com Santo')
