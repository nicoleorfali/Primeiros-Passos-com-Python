# Calculadora de tinta 
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
q_tinta = area/2
print(f'\nAs dimensões da parede são {largura}x{altura}m e sua área é de {area:.2f}m².\nVocê precisa de {q_tinta:.2f} litros de tinta.')
# para fazer o 2 de m² é só apertar o ALT da direita e o dois
