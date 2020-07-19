# Progressão aritmética

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 0
print('Os dez primeiros termos desta PA são: ', end='')
for i in range(1,11):
    termo = primeiro_termo + ((i - 1) * razao)
    print(termo, end=' ')
  