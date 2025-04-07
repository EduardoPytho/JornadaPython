def LeiaInt(msg=''):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print(f'ERRO, Você digitou um número inválido, tente outro!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n
def LeiaFloat(msg=''):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\31mNúmero inválido, tente outro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu digitar nada.')
        else:
            return n
number = LeiaInt('Digite o número: ')
num2 = LeiaFloat('Digite o número flutuante: ')
print(f'Você digitou o número inteiro {number}.')
print(f'Você digitou o número flutuante {num2}.')