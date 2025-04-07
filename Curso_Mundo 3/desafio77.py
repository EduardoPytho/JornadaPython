palavra = ('FUTURO','GRATIS','BOLSONARO')
for pals in palavra:
    print(f'\nA palavra {pals} tem as seguintes vogais: ',end='')
    for letras in pals:
        if letras in 'AEIOU':
            print(letras,end=' ')