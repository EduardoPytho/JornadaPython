from time import sleep
n50 = n20 = n10 = n1 = 0
print('\033[0;33m','-=-'*20,end=' ')
print('\033[1;33mBanco ValoraX: Made By Arthur Eduardo',end=' ')
print('\033[0;33m-=-'*20,'\033[m')
dinheiro = int(input('Deseja sacar quanto? \033[1;32mR$'))
print('\033[1;35mProcessando..','\033[m')
sleep(1)
while True:
    if dinheiro // 50 >0:
        n50 += 1
        dinheiro -= 50
    elif dinheiro // 20 >0:
        n20 += 1
        dinheiro -= 20
    elif dinheiro // 10 >0:
        n10 += 1
        dinheiro -= 10
    elif dinheiro // 1 >0:
        n1 += 1
        dinheiro -= 1
    elif dinheiro == 0:
        break
if n50 >= 1:
    print(f'Você irá sacar \033[0;33m{n50}\033[m Notas de \033[0;32m50 Reais','\033[m')
if n20 >= 1:
    print(f'Você irá sacar \033[0;33m{n20}\033[m Notas de \033[0;32m20 Reais','\033[m')
if n10 >= 1:
    print(f'Você irá sacar \033[0;33m{n10}\033[m Notas de \033[0;32m10 Reais','\033[m')
if n1 >= 1:
    print(f'Você irá sacar \033[0;33m{n1}\033[m Moedas de \033[0;32m1 Real','\033[m')