maior = 0
menor = 0
for pesos in range(1,6):
    n = float(input(f'{pesos}-Digite seu peso:'))
    if pesos == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(menor,maior)