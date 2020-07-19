'''João Pescador: Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. '''

peso = float(input('Qual o peso dos peixes (kg): '))
excesso = 0.0
multa = 0.0

if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
    print('Você excedeu o limite permitido em', excesso, 'kg')
    print('A multa a ser paga é de: R$', multa)
else:
    multa = 0
    print ('Peso dentro do limite permitido!')
    print ('Não há nenhuma multa.')

