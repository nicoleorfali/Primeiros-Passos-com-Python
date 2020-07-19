# Loja de tintas
# A cobertura da tinta é de 1 litro para cada 6 metros quadrados e a tinta é vendida em latas de 18 litros, que custam R$80,00 ou em galões de 3,6 litros, que custam R$25,00.

import math

area = float (input('Informe a área a ser pintada (m2): '))
quant_tinta = 1.1*(area/6) #quantidade de tinta necessária em litros, com quebra de 10%
print(f'A quantidade de tinta necessária é: {quant_tinta:.2f} litros')
latas = quant_tinta/18
galoes = (quant_tinta)/3.6
#math.ceil transforma o número real em inteiro, arredondando para cima
print ('A quantidade de latas necessárias é de', math.ceil (latas), 'latas, com custo de R$', math.ceil (latas)*80)
print ('A quantidade de galões necessárias é de', math.ceil(galoes), 'galões, com custo de R$', math.ceil (galoes)*25)
if (quant_tinta % 18) == 0:
    print ('A melhor opção de compra é:', (quant_tinta/18), 'latas, com custo de R$', (quant_tinta/18)*80)
else:
    diferenca = (quant_tinta%18)
    if (math.ceil(diferenca/3.6)*25)<80:
        print('Melhor opção de compra é:', math.floor(latas), 'latas e', math.ceil(diferenca/3.6), 'galões')
        print('Custo total de R$', (math.floor(latas)*80)+(math.ceil(diferenca/3.6)*25))
    else:
        print('Melhor opção de compra é:', math.ceil(latas), 'latas')
  