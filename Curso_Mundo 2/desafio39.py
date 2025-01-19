from datetime import date
from time import sleep
anoatual = int(date.today().year)
idade = int(input('\033[0;31mDigite seu ano de nascimento:\033[m '))
idades = anoatual-idade
faltando = int(((str(idades-18)).replace('-','')))
print('\033[1;35mProcessando..\033[m')
sleep(1)
if idades >100 or idade <1940:
    print('\033[1;31mEscolha um ano válido.\033[m')
    
elif idades == 17:
    print('\n\033[0;31mVocê ainda vai se alistar.\n')
    print(f'Falta \033[1;31m1 ano\033[m\033[0;31m para você se alistar,se prepare!\n')
    exit()
elif idades <18:
    print('\n\033[0;31mVocê ainda vai se alistar.\n')
    print(f'Falta \033[1;31m{faltando} anos\033[m\033[0;31m.\033[m\n')
    exit()
elif idades == 18:
    print('\033[0;32mEstá na hora de se \033[1;32malistar\033[m!\n')
    print('\033[0;32mVocê já tem \033[0;32m\033[1;32m18 anos\033[m\033[0;32m.\n')
    exit()
elif idades == 19:
    print(f'\033[0;31mJá passou da hora de se alistar.')
    print(f'você ultrapassou \033[1;31m1 ano\033[m\033[0;31m.')
    exit()
elif idades >=20:
    print(f'\033[0;31mJá passou da hora de se alistar.')
    print(f'você ultrapassou \033[1;31m{faltando} anos\033[m\033[0;31m.')
    exit()