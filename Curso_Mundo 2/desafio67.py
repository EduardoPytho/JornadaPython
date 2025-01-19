v = 0
log = '~~Criador de tabuada~~'
while True:
    num = int(input(f'{log:^65}\nDigite o valor (Digite um número negativo para terminar o programa): '))
    print('')
    for v in range(1,11):
        print(f'{num} X {v} = {num*v:^3}')
    if num <0:
        break
print('Programa fechado com sucesso.')