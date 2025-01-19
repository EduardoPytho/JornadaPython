from time import sleep
esc = str(input('Deseja iniciar a contagem agora? (\033[1;32mS\033[m/\033[1;31mN\033[m) ')).strip().upper()
if esc == 'S':
    for c in range(10,0, -1):
        print(f'\033[1;33m{c}\033[m')
        sleep(1)
    print('\033[1;32mFogos de artifício disparados com sucesso.\033[m')
if esc == 'N':
    print('\033[1;31mContagem cancelada com sucesso.\033[m')