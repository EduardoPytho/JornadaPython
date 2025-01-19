from random import randint
perdeu = False
par = False
impar = False
cv = 0
rn = randint(1,10)
while True:
    valor = int(input('Digite um valor: '))
    if valor >10 or valor <0:
        while True:
            valor = int(input('Valor inválido, digite um valor entre 1 e 10: '))
            if valor >0 and valor <10:
                break
    esc = str(input('Par ou Ímpar? (P/I) \n')).strip().upper()
    if esc != 'P' and esc != 'I':
        while True:
            esc = str(input('Sua escolha é inválida, escolha Par ou Ímpar. (P/I)\n')).strip().upper()
            if esc == 'P' or esc == 'I':
                break
    valores = rn+valor
    print(f'''Soma total: {valores}''')
    if valores % 2 == 0:
        par = True
    else:
        impar = True
    if esc == 'P' and par == True:
        print('O número é par, Parabéns, Você ganhou!!')
        cv += 1
    elif esc == 'I' and impar == True:
        print('O número é impar, Parabéns, Você ganhou!!')
        cv += 1
    elif esc == 'P' and par == False:
        print('O número é impar, Infelizmente você perdeu..\n\nFim do programa')
        perdeu = True
        break
    elif esc == 'I' and par == True:
        print('O número é par, Infelizmente você perdeu..\n\nFim do programa')
        perdeu = True
        break
if cv == 0:
    print('\nVocê ganhou nenhuma vez.. que má sorte ein.')
elif cv == 1:
    print('\nVocê ganhou uma vez, melhor do que nada yeah?')
elif cv >= 2:
    print(f'WOW! Você ganhou {cv} vezes, Você é bem sortudo!!')