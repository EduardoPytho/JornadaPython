soma = 0
contador = 0
for impares in range(1,501, 2):
    if impares % 3 == 0:
        contador = contador+1
        soma = soma+impares
print(f'A soma de todos os {contador} valores, são {soma}')