num = int(input('Escreva um número: '))
maior = num
menor = num
soma = 0
div = 0
esc = ''
while not esc == 'N':
    num = int(input('Escreva outro número: '))
    if num>maior:
        maior = num
    if num<menor:
        menor = num
    soma += num
    div += 1
    esc = str(input('Deseja escrever mais números? (S/N): ')).strip().upper()
med = soma/div
print(f'A média entre os números é {med}.\n')
print(f'O maior número digitado é o {maior}, e o menor digitado é o {menor}')