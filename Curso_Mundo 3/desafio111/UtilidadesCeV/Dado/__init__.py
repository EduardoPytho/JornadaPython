def moneyreader(ask='valor = '):
    entrada = str(input(ask)).strip().replace(',','.')
    if entrada.isalpha() or entrada == '':
        while True:
            entrada = input(f'\033[0;31mO valor "{entrada}" não é válido!\nTente outro: \033[m').strip().replace(',','.')
            if not entrada.isalpha() and entrada != '':
                break
    return float(entrada)