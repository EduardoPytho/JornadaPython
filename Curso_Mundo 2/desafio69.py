contagem_homens = mais_de_18 = mulheres_menos_de_20 = 0
gênero = ''
while True:
    idade_pessoas = int(input('\nInsira a idade da pessoa: '))
    gênero = str(input('\nInsira o gênero da pessoa (M/F): ')).strip().upper()[0]
    if gênero != 'M' and gênero != 'F':
        while 'M' not in gênero and 'F' not in gênero:
            gênero = str(input('\nInsira o gênero da pessoa (M/F): ')).strip().upper()[0]
    esc = str(input('\nDeseja continuar inserindo dados? (S/N): ')).strip().upper()[0]
    print('-_'*20)
    if gênero == 'M':
        contagem_homens += 1
    if idade_pessoas >18:
        mais_de_18 += 1
    if gênero == 'F' and idade_pessoas <20:
        mulheres_menos_de_20 += 1
    if esc == 'N':
        break
print(f'''Existe {contagem_homens} homem(s) nessa lista criada.
existe {mais_de_18} pessoa(s) com mais de 18 anos nessa lista.
existe {mulheres_menos_de_20} mulher(s) com menos de 20 anos nessa lista.''')