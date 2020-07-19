# Cálculo de ano bissexto
'''
Nota:
Para ser bissexto, o ano deve ser:
*   Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
*   Não pode ser múltiplos de 100 
*   Deve ser divisível por 400'''


from datetime import date
ano = int(input('Informe o ano que quer analisar. Coloque 0 se quiser o ano atual: '))
if ano == 0:
    ano = date.today().year  # pega o ano da data de hoje
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')
