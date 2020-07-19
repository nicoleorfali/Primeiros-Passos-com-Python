# Cálculo da Hipotenusa
from math import sqrt, pow, hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt(pow(oposto,2) + pow(adjacente,2))
print(f'O valor da hipotenusa é {hipotenusa}, fazendo a conta tradicional')
# OU
print(f'O valor da hipotenusa é {hypot(oposto,adjacente)}, usando a função da biblioteca math')
