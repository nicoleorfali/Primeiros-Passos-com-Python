# Calculadora 

print('{:=^40}'.format(' CALCULADORA DA NICOLE ')) #para centralizar a string
opcao = 0
print('''
[1] soma 
[2] multiplicação
[3] cálculo do maior
[4] novos números
[5] sair
''')
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
opcao = int(input('Informe a sua opção: '))
while opcao != 5:
  if opcao == 1:
    print(f'A soma de {n1} e {n2} é {n1 + n2}\n')
    opcao = int(input('Você deseja fazer outra operação: '))
  elif opcao == 2:
    print(f'A multiplicação de {n1} e {n2} é {n1 * n2}\n')
    opcao = int(input('Você deseja fazer outra operação: '))
  elif opcao == 3:
    if n1 > n2:
      print(f'O maior número entre {n1} e {n2} é {n1}\n')
    elif n1 < n2:
      print(f'O maior número entre {n1} e {n2} é {n2}\n')
    else:
      print(f'Os números são iguais!\n')
    opcao = int(input('Você deseja fazer outra operação: '))
  elif opcao == 4:
    n1 = float(input('Informe o primeiro novo número: '))
    n2 = float(input('Informe o segundo novo número: '))
    opcao = int(input('Qual a operação desejada: '))
  else:
    print('Opção inválida!')
    opcao = int(input('Informe sua opção: '))
print('\nFim do Programa! Até logo!!!')
    