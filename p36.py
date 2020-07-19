# Análise de tipos de triângulos

print('-='*30)
print(f'Analisador de Triângulos e seus Lados')
print('-='*30)
s1 = int(input('Digite o tamanho do primeiro segmento: '))
s2 = int(input('Digite o tamanho do segundo segmento: '))
s3 = int(input('Digite o tamanho do terceiro segmento: '))

if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
    print(f'Os segmentos de medida {s1}, {s2} e {s3} podem formar um triângulo ', end='') # o end dessa forma não deixa quebrar a linha
    if s1 == s2 == s3:             #Python aceita desta maneira
        print(f'Equilátero')
    elif s1 != s2 != s3 != s1:  #Python aceita desta maneira
        print(f'Escaleno')
    else:
        print(f'Isósceles')
else:
    print(f'Os segmentos de medida {s1}, {s2} e {s3} não podem formar um triângulo')
