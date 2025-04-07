valores = []
while True:
    valores.append(int(input('Insira um valor: ')))
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if escolha == 'N':
        print('Finalizado.\n')
        break
print(f'Você digitou {len(valores)} Números')
print(f'\nLista em ordem descrecente: {sorted(valores, reverse=True)}\n')
if 5 not in valores:
    print('O número 5 não foi encontrado na lista!')
else:
    print('O número 5 foi encontrado na lista!\nNas posições: ',end='')
    for pos,valor in enumerate(valores):
        if valor == 5:
            print(pos,end=' ')
print('\n')