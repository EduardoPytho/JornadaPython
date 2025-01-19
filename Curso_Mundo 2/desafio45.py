from random import choice

from time import sleep

lista = ['Pedra','Papel','Tesoura']

r = choice(lista)

jogo = str(input('\033[0;33m====== Pedra,Papel e Tesoura ======\n\n\033[0;34mEscreva qual objeto você quer:\n\033[1;34m')).upper().strip()

print('\033[1;35mProcessando..')

sleep(0.5)

#Perdendo

if 'Papel' in r and 'PEDRA' in jogo:

    print('\033[0;31mPapel! \033[1;31mVocê perdeu!\033[m')

elif 'Tesoura' in r and 'PAPEL' in jogo:

    print('\033[0;31mTesoura! \033[1;31mVocê perdeu!\033[m')

elif 'Pedra' in r and 'TESOURA' in jogo:

    print('\033[0;31mPedra! \033[1;31mVocê perdeu!\033[m')

#Ganhando

elif 'Papel' in r and 'TESOURA' in jogo:
    print('\033[0;32mPapel! \033[1;32mOh no! Você ganhou!\033[m')

elif 'Pedra' in r and 'PAPEL' in jogo:

    print('\033[0;32mPedra! \033[1;32mOh no! Você ganhou!\033[m')

elif 'Tesoura' in r and 'PEDRA' in jogo:
    
    print('\033[0;32mTesoura! \033[1;32mOh no! Você ganhou!\033[m')

elif r == jogo:
    print(f'\033[0;34m{jogo}, Oh no! empate!')

else:
    print(f'\033[1;31mObjeto invádido.')