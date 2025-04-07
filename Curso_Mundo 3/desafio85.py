lista = [[],[]]
# primeira = par, segunda = ímpar
for c in range(1,8):
    valor = int(input(f'Valor {c}: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Lista de pares = {sorted(lista[0])}\nLista de ímpares = {sorted(lista[1])}.')