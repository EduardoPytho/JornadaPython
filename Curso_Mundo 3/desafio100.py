from random import randint
from time import sleep
lista_números = list()
def lin():
    print('-='*25)
def sorteia(lis_num):
    c = 0
    while c <5:
        lis_num.append(randint(1,10))
        c += 1
    print('Sorteando os números..')
    for numeros in lis_num:
        sleep(0.5)
        print(numeros,end=' ',flush=True)
    print('')
def somaPar(lista):
    pares = 0
    for num in lista:
        if num % 2 == 0:
            pares+=num
    print(f'Números sorteados: {lista}, se somar só os pares iria ficar {pares}.')


lin()
sleep(0.5)
sorteia(lista_números)
sleep(0.5)
lin()
sleep(0.5)
somaPar(lista_números)
sleep(0.5)
lin()