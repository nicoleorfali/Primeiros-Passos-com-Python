# Manipulação de strings
frase  = str(input('Digite uma frase: ')).strip() #strip tirando espaços indesejáveis
f = frase.upper()
print('Número de vezes que a letra A aparece na frase:' , f.count('A'))
print('Posição onde A aparece pela primeira vez:', f.find('A') + 1) #começa na posição 0
print('Posição onde A aparece pela última vez:', f.rfind('A') + 1) #função find adionada de r, para começar pela direita
