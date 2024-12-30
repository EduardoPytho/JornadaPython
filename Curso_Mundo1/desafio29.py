km = int(input('\n\nDigite a velocidade de seu carro: '))
if km >80:
    km = (km-80)*7.00
    print(f'\nVocê foi multado em R${km:.2f}\n')
else:
    print('\nParabéns! Você não foi multado pois não ultrapassou a velocidade de 80 Km/H.\n')
print('Fim..')