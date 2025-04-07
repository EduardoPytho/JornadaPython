valores = []
posições_maiores = []
posições_menores = []
for v in range(0,5):
    valores.append(int(input(f'Digite o valor para a posição {v}: ')))
    if v == 0:
        posições_maiores = posições_menores = valores[v]
    else:
        if valores[v]>posições_maiores:
            posições_maiores = valores[v]
        if valores[v]<posições_menores:
            posições_menores = valores[v]
print('-='*30)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi o {max(valores)}, e ele está nas posições.. ',end='')
for p,v in enumerate(valores):
    if v == posições_maiores:
        print(f'{p}..',end='')
print()
print(f'O menor número digitado foi o {min(valores)}, e ele está nas posições..',end='')  
for pm,v in enumerate(valores):
    if v == posições_menores:
        print(f'{pm}..',end='')