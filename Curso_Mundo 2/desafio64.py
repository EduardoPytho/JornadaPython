esc = 0
soma = 0
cont = 0
while not esc == 999:
    esc = int(input('\033[mDigite um número (digite 999 para parar.): \033[0;33m'))
    print('')
    soma += esc
    cont += 1
print(f'Você digitou {cont} números, e a soma entre todos eles são {soma}')
