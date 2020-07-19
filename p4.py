# Programa que lê informação do usuário e retorna informações relacionadas
inf = input('Digite alguma coisa: ')  #função input sempre retorna string
print(f'O tipo primitivo deste valor é {type(inf)}')
print(f'Só tem espaços? {inf.isspace()}')
print(f'É um número? {inf.isnumeric()}')
print(f'É alfabético? {inf.isalpha()}')
print(f'É um alfanumérico? {inf.isalnum()}')
print(f'Está em maiúscula? {inf.isupper()}')
print(f'Está em minúscula? {inf.islower()}')
print(f'Está capitalizado? {inf.istitle()}')
