from random import randint
from time import sleep

número = randint(1,5)

print('-/-' * 10,'JOGO DA ADIVINHAÇÃO','-/-' * 10)

p = int(input('\nEscolha um número de 1 a 5: '))

print('\nProcessando...')
sleep(2.5)

if p == número:
    print('\nParabéns! Você acertou o número!\n')
else:
    print('\nVocê errou o número!\n')
print('Fim de jogo..')