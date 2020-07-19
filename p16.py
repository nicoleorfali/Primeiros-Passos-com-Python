# Sorteio de alunos 
from random import choice, shuffle

nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')
alunos = [nome1, nome2, nome3, nome4]
escolhido = choice(alunos)
print(f'O aluno escolhido para apagar o quadro é: {escolhido}')
shuffle(alunos)
print(f'A ordem de apresentação dos trabalhos é: ', alunos)
