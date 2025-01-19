from random import randint
from time import sleep
tt = 1
número = randint(1,10)

print('-/-' * 10,'JOGO DA ADIVINHAÇÃO','-/-' * 10)

p = int(input('\nEscolha um número de 1 a 10: '))

print('\nProcessando...')
sleep(1.5)

if p == número:
    print('\nParabéns! Você acertou o número! conseguiu de primeira, você é profissional!!\n')
else:
    print('\nVocê errou o número!')
    while p != número:
        if p>número:
            dica = 'Menos'
        elif p<número:
            dica = 'Mais'
        print(f'\nÉ {dica}..')
        p = int(input('''\nTente novamente! vou te dar mais chances.
digite outro número:'''))
        if p>número:
            dica = 'Menos'
        elif p<número:
            dica = 'Mais'
        tt += 1
        print('\nProcessando...')
        sleep(1.5)
        if p == número:
            print(f'\nParabéns, você acertou depois de {tt} tentativas!')
print('\nFim de jogo..\n')