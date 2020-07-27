# Análise da necessidade de voto

# Definindo a função
def voto(ano):
    from datetime import date   #será usado apenas dentro da função
    ano_atual = date.today().year  
    idade = ano_atual - ano
    if 65 > idade >= 18:
        print(f'Idade {idade} -> Voto OBRIGATÓRIO')
    elif idade >= 65 or 16 <= idade < 18:
        print(f'Idade {idade} -> Voto OPCIONAL')
    else:
        print(f'Idade {idade} -> Voto NEGADO')    


# Programa principal
inf = int(input('Digite o ano que você nasceu: '))
voto(inf)
