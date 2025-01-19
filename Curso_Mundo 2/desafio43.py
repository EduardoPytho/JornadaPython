altura = str(input('Digite sua altura em metros: \033[0;33m')).strip().replace(',','.')
altura = float(altura)
if altura <=0.0:
    print('\033[1;31mERRO. Sua altura tem ou possui menos de 0.\033[m')
    exit()
kg = str(input('\033[mDigite seu peso em Kilos: \033[0;33m')).strip().replace(',','.')
kg = float(kg)
if kg <=0.0:
    print('\033[1;31mERRO. Seu peso tem ou possui menos de 0.\033[m')
    exit()
IMC = kg/(altura**2)
if IMC <0:
    print('\033[1;31mERRO, Seu IMC tem ou possui menos de 0.')
elif IMC <18.5 and IMC >0:
    print(f'\033[1;36mIMC: {IMC:.2f}\033[m, Seu status é \033[1;36mAbaixo do Peso\033[m.')
elif IMC >=18.5 and IMC <25:
    print(f'\033[1;34mIMC: {IMC:.2f}\033[m, Seu status é \033[1;34mPeso ideal\033[m.')
elif IMC >=25 and IMC <30:
    print(f'\033[1;35mIMC: {IMC:.2f}\033[m, Seu status é \033[1;35mSobrepeso\033[m.')
elif IMC >=30 and IMC <40:
    print(f'\033[1;33mIMC: {IMC:.2f}\033[m, Seu status é \033[1;33mObesidade\033[m.')
elif IMC >=40 and IMC <130:
    print(f'\033[1;31mIMC: {IMC:.2f}\033[m, Seu status é \033[1;31mObesidade mórbida\033[m.')
else:
    print(f'\033[1;31mERRO. Seu IMC é impossível de possuir, ou é 100% mortal.')