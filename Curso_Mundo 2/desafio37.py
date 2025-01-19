num = int(input('Digite um número inteiro: \033[0;33m'))
print('''\033[mEscolha uma das bases para conversão:\033[0;32m

[1] Binário
[2] Octal
[3] Hexadecimal\033[m
''')
dig = int(input('Digite: \033[0;33m'))
if dig == 1:
    print(f'\033[mO número \033[1;33m{num}\033[m convertido para binário é \033[1;33m{bin(num)[2:]}\033[m')
elif dig == 2:
    print(f'\033[mO número \033[1;33m{num}\033[m convertido para octal é \033[1;33m{oct(num)[2:]}\033[m')
elif dig == 3:
    print(f'\033[mO número \033[1;33m{num}\033[m convertido para hexadecimal é \033[1;33m{hex(num)[2:]}\033[m')
else:
    print('\033[1;31mNúmero digitado inválido.\033[m')