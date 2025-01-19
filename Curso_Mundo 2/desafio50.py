junt = 0
consi = 0
desco = 0
for pgt in range(1,7):
    print(f'{pgt}- ',end='')
    valor = int(input('Digite um valor:\033[0;33m'))
    print('\033[m')
    if valor%2 == 0:
        junt = junt+valor
        consi = consi+1
    else:
        desco = desco+1
print(f'Somando os pares, o resultado seria {junt}')
print(f'''{consi} foram Considerados.
{desco} foram Desconsiderados.''')