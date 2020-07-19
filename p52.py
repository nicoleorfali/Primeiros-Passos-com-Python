# Vogais em palavras - usando tuplas

palavras = ('Sacola', 'Lençol', 'Sacada', 'Mouse', 'Computador', 'Python', 'Menino', 'Desenho', 'Amarelo', 'Dados' )
for p in palavras:
  print(f'\nNa palavra {p.upper()} temos as seguintes vogais: ', end = '')
  for letra in p:
    if letra.lower() in 'aeiou':
     print(f'{letra.upper()} ', end = '')
