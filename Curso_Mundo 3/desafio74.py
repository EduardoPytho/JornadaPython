from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
print(f'Os números sorteados foram o: ',end='')
for n in num:
    print(f'{n} ',end='')
print(f'\n\nMaior = {max(num)}')
print(f'\nMenor = {min(num)}\n')