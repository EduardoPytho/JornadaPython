soma = valores = 0
while True:
    num = int(input('Digite um valor (Digite 999 para terminar): '))
    soma += num
    valores += 1
    if num == 999:
        break
print(f'A soma de todos os {valores} valores digitados é {soma}')