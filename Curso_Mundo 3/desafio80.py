valores_ordenados = []
posi = 0
contagem = 1
for c in range(0,5):
    valor = int(input('Insira o valor: '))
    if c == 0 or valor>max(valores_ordenados):
        print('Adicionado ao final da lista..')
        valores_ordenados.append(valor)
    else:
        while posi < len(valores_ordenados):
            if valor <= valores_ordenados[posi]:
                valores_ordenados.insert(posi,valor)
                break
            posi += 1
        print(f'Adicionado na posição {posi}..')
print('-='*40)
print(f'Lista ordenada crescentemente: {valores_ordenados}')