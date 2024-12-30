from random import suffle
a1 = str(input('Nome 1: '))

a2 = str(input('Nome 2: '))

a3 = str(input('Nome 3: '))

a4 = str(input('Nome 4: '))

lista = [a1,a2,a3,a4]

ra = suffle (lista)

print(f'A ordem será {lista}')