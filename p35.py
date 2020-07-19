# Análise de categoria dos atletas

from datetime import date

ano = int(input('Informe o ano em que você nasceu: '))
ano_corrente = date.today().year  # pega o ano da data de hoje
idade = ano_corrente - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos e está na categoria MIRIM.')
elif idade <= 14:
   print(f'O atleta tem {idade} anos e está na categoria INFANTIL.') #não precisa botar intervalo pq ele so chega aqui se nao satisfizer anterior 
elif idade <= 19:
   print(f'O atleta tem {idade} anos e está na categoria JUNIOR.')
elif idade <= 25:
   print(f'O atleta tem {idade} anos e está na categoria SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos e está na categoria MASTER.')
