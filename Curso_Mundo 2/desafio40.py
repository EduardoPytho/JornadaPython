from time import sleep
n1 = float(input('\033[0;33mQuanto você tirou na primeira prova? \033[7;0mNota: '))
n2 = float(input('\033[0;33mQuanto você tirou na segunda prova?  \033[7;0mNota: '))
média = (n1+n2)/2
print('\033[m\033[1;35mProcessando..\033[m')
sleep(1.3)
if média >10:
    print('\033[1;31mSua média ultrapassou o limite de 10, Escolha sua nota \033[1;31mREAL\033[m\033[0;31m.\033[m')
elif média <5.0:
    print(f'\033[m\033[1;31mMédia: {média}\033[m, \033[0;31mInfelizmente, Você foi reprovado.\033[m\n')
elif média >=5.0 and média <=6.9:
    print(f'\033[m\033[1;33mMédia: {média}\033[m, \033[0;33mInfelizmente você está de recuperação, Boa sorte!\033[m')
elif média >=7.0 and média <=10:
    print(f'\033[1;32mMédia: {média}\033[m, \033[0;32mParabéns! Você passou de ano por média!\033[m')