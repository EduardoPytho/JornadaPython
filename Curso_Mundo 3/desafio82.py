valores = []
pares = []
impares = []
while True:
    valor = int(input('Insira um valor: '))
    valores.append(valor)
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if escolha == 'N':
        print('Finalizado.\n')
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Lista normal: {valores}\nLista somente com pares: {pares}\nLista somente com ímpares: {impares}')