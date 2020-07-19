# Radar eletrônico: caso o usuário esteja acima de 80km/h, será multado em R$7 por km acima do limite

v = float(input(('Informe a velocidade do carro em km/h: ')))
if v > 80:
  multa = (v - 80) * 7
  print(f'Usuário está acima da velocidade permitida')
  print(f'O valor da multa é R${multa:.2f}')
else:
  print('Velocidade dentro do limite permitido. \nBoa viagem! Dirija com cuidado.')
