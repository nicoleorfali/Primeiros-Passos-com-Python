# Conversor de base

numero = int(input('Informe um número inteiro: '))
print('''Escolha a base de conversão:
[1] Para BINÁRIO
[2] Para OCTAL
[3] Para HEXADECIMAL''')
opcao = int(input('Informe a base escolhida: '))
if opcao == 1:
    print(f'{numero} convertido em BINÁRIO é {bin(numero)[2:]}') #[2:] fatia a string e tira o 0b inicial, que indica que é binário
elif opcao == 2:
    print(f'{numero} convertido em OCTAL é {oct(numero)[2:]}') #[2:] fatia a string e tira o 0o inicial, que indica que é octal
elif opcao == 3:
    print(f'{numero} convertido em HEXADECIMAL é {hex(numero[2:])}') #[2:] fatia a string e tira o 0h inicial, que indica que é hexadecimal
else:
    print(f'Você digitou {numero}, o que é uma opção inválida. \nTente novamente!!!') 