sexo = str(input('Insira seu sexo (M/F): ')).strip().upper()
if sexo != 'M' or sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Insira novamente:')).strip().upper()
print('Salvo com sucesso.')