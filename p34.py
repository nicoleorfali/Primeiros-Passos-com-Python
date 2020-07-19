# Média escolar

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7:
    print(f'A média é {media:.2f} e o aluno(a) foi APROVADO(A)!!! ')
elif media < 5:
    print(f'A média é {media:.2f} e o aluno(a) foi REPROVADO(A)!!! ')
else:
    print(f'A média é {media:.2f} e o aluno(a) está em RECUPERAÇÃO!!! ')
