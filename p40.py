# Contagem regressiva - Virada de ano

from time import sleep

print('{:=^31}''\n'.format(' CONTAGEM REGRESSIVA ')) #para centralizar a string
for i in range(10,0,-1):
  print('{:^31}'.format(i))
  sleep(1)
print('{:^31}'.format('FELIZ ANO NOVO!!!'))
