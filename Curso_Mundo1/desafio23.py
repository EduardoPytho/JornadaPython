número = int(input('Escolha um número de 1 a 9999, e escreva: '))

u = número // 1 % 10

d = número // 10 % 10

c = número // 100 % 10

m = número // 1000 % 10

print(f'Unidade = {u}\nDezena = {d}\nCentena = {c}\nMilhar = {m}')