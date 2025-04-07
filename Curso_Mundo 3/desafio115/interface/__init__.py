def leiainteiro(msg=''):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print(f'\033[31mERRO, Você digitou um número inválido, tente outro!\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n

def lin(tam=42):
    return '-'*tam

def logo(txt='Olá Mundo!'):
    print(lin())
    print(txt.center(42))
    print(lin())

def menu(*lista):
    logo('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}- \033[34m{item}\033[m')
        c+=1
    print(lin())
    opc = leiainteiro('\033[32mSua Opção: \033[m')
    return opc

#print('\033[33m1- \033[33mCadastrar')
#print('\033[33m2- \033[32mEntrar')
#print('\033[33m3- \033[32mSair do sistema\033[m')