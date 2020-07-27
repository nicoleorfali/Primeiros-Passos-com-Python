# Função Leitura de Tela

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro. Digite um inteiro')
        if ok:
            break
    return valor


num = leiaint('Digite um número inteiro: ')
print(f'Você digitou {num}')