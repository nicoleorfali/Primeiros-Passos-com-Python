# Loja - opções de pagamento

print('{:=^40}'.format(' LOJAS NICOLE ')) #para centralizar a string
valor = float(input('Informe o valor do produto: R$ '))
print('''Escolha a opção de pagamento:
[1] À vista com dinheiro ou cheque (10% de desconto)
[2] À vista no cartão de crédito (5% de desconto)
[3] Em 2x no cartão de crédito (valor normal)
[4] 3x ou mais no cartão de crédito (20% de juros)\n''')
opcao = int(input('Informe a sua opção: '))

if opcao == 1:
    print(f'O valor da compra de R${valor:.2f} sairá R${(valor * 0.9):.2f} à vista com dinheiro ou cheque')
elif opcao == 2:
    print(f'O valor da compra de R${valor:.2f} sairá R${(valor * 0.95):.2f} à vista no cartão de crédito')
elif opcao == 3:
    print(f'O valor da compra é de R${valor:.2f} em 2x no cartão de crédito')
    print(f'O valor das parcelas será R${(valor/2):.2f}')
elif opcao == 4:
    parcelas = int(input('Número de parcelas: '))
    print(f'O valor da compra é de R${valor:.2f} sairá por R${(valor * 1.2):.2f} em {parcelas} vezes')
    print(f'O valor de cada parcela será R${((valor * 1.2)/parcelas):.2f}')
else:
    print('Você escolheu uma opção inválida.\nPor favor, tente novamente!')
