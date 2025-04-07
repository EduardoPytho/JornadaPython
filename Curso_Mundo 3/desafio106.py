from time import sleep
def manual(comando='print'):
    return help(comando)

def titulo():
    print('\033[1;30m','-=' * 60)
    print('\033[1;0;43m','-'*20,' PyHelp ','-'*20,'\n')
while True:
    titulo()
    comando = str(input('\033[mPor favor, Digite a biblioteca ou comando: '))
    if comando.upper() == 'FIM':
        break
    print('-='*60)
    print(f'\033[0;30;46m','~~'*10,f'Acessando o manual do {comando}..','~~'*10)
    sleep(2)
    print('\n\033[1;30;47m',end='')
    print(manual(comando))
    sleep(1)
print('\nLeitor de manual finalizado com sucesso!')