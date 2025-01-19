from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
esc = 0
while esc != 5:
    sleep(0.5)
    print('=-'*10)
    esc = int(input('''O que você quer fazer?

[1] Somar os números
[2] Multiplicar os números
[3] Maior e Menor número
[4] Novos números
[5] Sair do Programa

Digite: '''))
    print('=-'*10)
    if esc == 1:
        n = n1+n2
        print(f'\nA soma do número {n1} e {n2} fica {n}\n')
    elif esc == 2:
        n = n1*n2
        print(f'A multiplicação entre {n1} e {n2} é {n}')
    elif esc == 3:
        if n1>n2:
            print(f'O número {n1} é maior que o número {n2}.')
        elif n2>n1:
            print(f'O número {n2} é maior que o número {n1}.')
    elif esc == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
print('Fim do programa.')