# Lista de Preços na Papelaria

listagem = ('Lápis', 1.75, 'Borracha', 2.96, 'Caderno', 15.90 , 
            'Estojo', 25.3, 'Transferidor', 3.7, 'Compasso', 12, 
            'Mochila', 120.5, 'Caneta', 9.8, 'Livro', 78.9 )
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # para formatar string, usar "" para diferenciar
print('='*40)
for i in range(0, len(listagem)):
  if i % 2 == 0:
    print(f'{listagem[i]:.<30}', end='')
  else:
    print(f'R${listagem[i]:>7.2f}') #em sete espaços centralizado a direita, com duas casa
print('='*40)
