dadosTemp = []
dadosFore = []
maior = menor = 0
while True:
    dadosTemp.append(str(input('Nome: ')))
    dadosTemp.append(float(input('Peso: ')))
    if len(dadosFore) == 0:
        maior = menor = dadosTemp[1]
    else:
        if dadosTemp[1]>maior:
            maior = dadosTemp[1]
        elif dadosTemp[1]<menor:
            menor = dadosTemp[1]
    dadosFore.append(dadosTemp[:])
    dadosTemp.clear()
    escolha = str(input('Deseja continuar inserindo? [S/N]: ')).strip().upper()
    if escolha == 'N':
        break
print('-='*60)
print(f'No total, Foram digitados {len(dadosFore)} dados de usuários.')
print(f'O maior peso digitado foi o de {maior} Quilos. de: ',end='')
for p in dadosFore:
    if p[1] == maior:
        print([p[0]],end=' ')
print(f'\nE o menor peso digitado foi o de {menor} Quilos. de: ',end='')
for p in dadosFore:
    if p[1] == menor:
        print([p[0]],end=' ')
print('\n','-='*60)