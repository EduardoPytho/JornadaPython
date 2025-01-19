from time import sleep
num = int(input('Escreva um número para a tabuada:'))
ind = int(input('Indo até:'))
nada = 0
for tab in range(num,num*ind+1, num):
    if tab % num == 0:
        nada = nada + 1
    print(f'{num}x{nada} = {tab}')
    sleep(0.2)