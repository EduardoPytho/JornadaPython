ano = int(input('Escreva um ano e eu irei falar se ele é bissexto ano:'))
par = ano%4
if par == 0 and ano%100 != 0 or ano%400 == 0:
    print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')
print('\n\n==Fim==\n')