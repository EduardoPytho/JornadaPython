frase = str(input('Escreva uma frase ou palavra:')).strip().upper().replace(' ','')
inverso = frase[::-1]
if inverso == frase:
    print('Essa frase/palavra é palindroma')
else:
    print('Essa frase/palavra não é palindroma')