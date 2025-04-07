n1 = int(input('1-Digite um valor: '))
n2 = int(input('2-Digite mais outro valor: '))
n3 = int(input('3-Digite mais um valor: '))
n4 = int(input('4-Digite o último valor: '))
lista = (n1,n2,n3,n4)
print(f'Você digitou os valores {lista}.\n')
print(f'o 9 apareceu {lista.count(9)} vezes.\n')
if 3 in lista:
    print(f'O 3 apareceu na {lista.index(3)+1}° Posição')
else:
    print('O 3 apareceu em nenhuma posição.\n')
print(f'Os números pares digitados são o ',end='')
for c in lista:
    if c % 2 == 0:
        print(f'{c} ',end='')