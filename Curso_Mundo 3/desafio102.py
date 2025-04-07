from math import factorial
def fact(num=10,show=False):
    """
    :param num: Número para mostrar o seu Fatorial.
    :param show: True ou False, se for True, mostra o cálculo.
    :return: os 2 retornam o resultado.
    """
    if show:
        for c in range(1,num+1):
            if c == 1:
                print(c,end=' ')
            c += 1
            print(f'x {c}',end=' ')
        print(f'= ',end='')
        return factorial(num)
    else:
        return factorial(num)

print('-'*15)
print(fact(9,True))
print('')
print(help(fact))