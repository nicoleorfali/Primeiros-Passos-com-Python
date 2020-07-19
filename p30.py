# Analisador de empréstimo bancário

valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o valor do seu salário: R$'))
tempo = float(input('Informe em quantos anos a casa será paga: '))
mensalidade = valor / (tempo * 12)
if mensalidade <= (salario * 0.3):
    print(f'Seu impréstimo foi APROVADO!\nO valor da mensalidade será R${mensalidade:.2f}')
else:
    print('Seu empréstimo foi NEGADO!')
