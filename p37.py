# Cálculo de IMC

peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f'O IMC é de {imc:.2f}\nVocê está Abaixo do Peso')
elif imc <= 25:
     print(f'O IMC é de {imc:.2f} \nVocê está no Peso Ideal') # também dá para fazer: elif 18.5 <= imc < 25
elif imc <= 30:
   print(f'O IMC é de {imc:.2f} \nVocê está com Sobrepeso')
elif imc <= 40:
    print(f'O IMC é de {imc:.2f} \nVocê está com Obesidade')
else:
    print(f'O IMC é de {imc:.2f} \nVocê está com Obesidade Mórbida. CUIDADO!!!')
