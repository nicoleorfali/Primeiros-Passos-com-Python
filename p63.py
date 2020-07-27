# Unindo dicionários e listas

pessoa = {}
galera = []
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True: 
        pessoa['sexo'] = str(input('Sexo (M ou F): ')).upper()[0] #coloca em maiúscula e pega primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')
    if resp == 'N':
        break
print('-='*31)
print(f'Ao todos temos {len(galera)} pessoas cadastradas.')
média = soma/len(galera)
print(f'A média de idade é {média:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='  ')
print()   
print('Lista de pessoas acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<PROGRAMA ENCERRADO>>')