# Alistamento Militar 

from datetime import date

ano = int(input('Informe o ano em que você nasceu: '))
ano_corrente = date.today().year  # pega o ano da data de hoje
mes_corrente = date.today().month
idade = ano_corrente - ano 
if idade < 18:
    print(f'Você tem {idade} anos. Faltam {18 - idade} ano(s) para alistamento.')
elif idade > 18:
    print(f'Você tem {idade} anos.  Já passou do tempo para alistamento.')
else:
    print(f'Você tem {idade} anos. Você deve ser alistar este ano!!!')
