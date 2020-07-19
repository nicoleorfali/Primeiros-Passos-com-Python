# Cálculo de custos de viagem

d = float(input('Informe a distância em km:  '))
if d <= 200:
  custo = d * 0.5
else:
  custo = d * 0.45
print(f'O custo da viagem será de R${custo:.2f}')

#também dá para fazer if simplificado
# custo = d * 0.5 if d<=200 else d *