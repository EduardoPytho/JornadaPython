from datetime import date
from time import sleep
ano = date.today().year
anodenascimento = int(input('Digite seu ano de nascimento:\033[0;33m '))
idade = ano - anodenascimento
sleep(0.5)
print('\033[1;35mProcessando..\033[m')
sleep(2)
if idade >125:
    print('\033[1;31mVocê ultrapassou o limite de idade.\033[m')
elif idade >=0 and idade <=9:
    print('Sua categoria é \033[1;33mMIRIM\033[m\033[0;33m.\033[m')
elif idade <=14:
    print('Sua categoria é \033[1;33mINFANTIL\033[m\033[0;33m.\033[m')
elif idade <=19:
    print('Sua categoria é \033[1;33mJUNIOR\033[m\033[0;33m.\033[m')
elif idade <=20:
    print('Sua categoria é \033[1;33mSÊNIOR\033[m\033[0;33m.\033[m')
elif idade >20 and idade <=125:
    print('Sua categoria é \033[1;33mMASTER\033[m\033[0;33m.\033[m')
else:
    print('\033[1;31mOcorreu um erro ao tentar processar.\033[m')