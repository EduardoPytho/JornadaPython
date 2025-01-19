from math import factorial
nu = int(input('Insira seu número:\033[0;33m'))
nu1 = nu-1
print(f'{nu}x{nu1}x',end='')
while nu1 != 1:
    nu1 -= 1
    print(f'{nu1}x',end='')
frac = factorial(nu)
print(f'0 = \033[1;33m{frac}\033[m')