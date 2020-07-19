# ANálise de maioridade

from datetime import date
soma = 0
ano_atual = date.today().year
for i in range(5):
    ano = int(input('Digite o ano de nascimento: '))
    if (ano_atual - ano) < 18:
        soma += 1
print(f'{soma} pessoas ainda não atingiram a maioridade ')