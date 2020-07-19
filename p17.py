# Manipulação de strings
print('_______________________________________________________________________________')
nome = str(input('Digite o seu nome: ')).strip()  # strip elimina eventuais espaços inúteis de inicio e fim inseridos pelo usuário
print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
print(f'Seu nome em letras minúsculas é: {nome.lower()}')
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' '))) #contando os espaços vazios
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
#OU
#print(f'Seu primeiro nome tem {nome.find(' ')}) #a função find retorna a posição do primeiro argumento informado na string
#Como o espaço vem depois do nome e a contagem começa em 0, o número informado por find será igual ao tamanho do primeiro nome
