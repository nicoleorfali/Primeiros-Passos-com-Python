# Analisador de Triângulos

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
s1 = int(input('Digite o tamanho do primeiro segmento: '))
s2 = int(input('Digite o tamanho do segundo segmento: '))
s3 = int(input('Digite o tamanho do terceiro segmento: '))
if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
    print(f'\nOs segmentos de medida {s1}, {s2} e {s3} podem formar um triângulo')
else:
    print(f'\nOs segmentos de medida {s1}, {s2} e {s3} não podem formar um triângulo')
