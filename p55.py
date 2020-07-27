# Cálculo de fatorial

def fatorial(num, show=False):
    """
    Calcula o fatorial de um número, 
    onde num é o número cujo fatorial sera calculado
    e show mostra o cálculo realizado.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show: 
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    print(f)
    return f
 
 # Programa principal
x = int(input('Informe o número para cálculo de fatorial: '))
fatorial(x, True)