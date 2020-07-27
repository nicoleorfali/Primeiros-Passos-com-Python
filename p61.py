# Cadastro do Trabalhador

from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))

dados['idade'] = datetime.today().year - nasc  #também dá pra usar datetime.now().year
dados['CTPS'] = int(input('Carteira de trabalho (0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário R$: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35) - datetime.now().year
print('=='*30)
for i, j in dados.items():
    print(f'{i} tem valor {j}')