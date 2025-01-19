from time import sleep
cont = 0
num = int(input('\nDigite um número:\033[0;33m'))
esc = str(input('\033[mQuer ver o processo? (S/N): ')).upper().strip()
if esc == 'S':
    for primo in range(1,num+1):
        if num % primo >0:
           sleep(0.02)
           print(f'\033[1;31m{num}\033[0;31m não é divisivel por \033[1;31m{primo}\n')
        elif num % primo == 0:
            cont += 1
            sleep(0.2)
            print(f'\033[1;32m{num}\033[0;32m é divisivel por \033[1;32m{primo}\n')

else:
    print('Visualização de processo cancelada.')
    for primo in range(1,num+1):
        if num % primo == 0:
            cont += 1
print(f'\n\033[0;33mO número \033[1;33m{num}\033[0;33m é divisível por \033[1;33m{cont}\033[0;33m números.\n')
if cont == 2:
    print('\n\033[1;32mSeu número é primo.\033[m')
else:
    print('\n\033[1;31mSeu número NÃO é primo.\033[m\n')