def área(lg,cm):
    area = lg*cm
    print(f'A área de {lg}x{cm} é {area:.1f}m²')
largura = float(input('Largura: \033[0;33m'))
comprimento = float(input('\033[mComprimento: \033[0;33m'))
área(largura,comprimento)
print('\033[m')