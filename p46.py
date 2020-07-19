# Analisando Palíndromos

frase = str(input('Digite uma frase qualquer: '))
frase2 = frase.replace(' ', '').lower() #tira os espaços e põe em minúsculas
palin = ''
for i in range(1,len(frase2)+1):
    palin += frase2[-i]
if frase2 == palin:
    print('PALÍNDROMO')
else:
    print('NÃO PALÍNDROMO')
